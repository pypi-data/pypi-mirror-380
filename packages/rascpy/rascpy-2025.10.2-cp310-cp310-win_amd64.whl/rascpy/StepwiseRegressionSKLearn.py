# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 09:18:16 2025

@author: wangwenhao
"""
import numpy as np
import pandas as pd
from .Index import KS,VIF,SCORERS
import statsmodels.api as sm
from .Tool import parse_x_group,get_gsplit_gindex#,predict_proba
from .Lan import lan
from scipy import stats
import os
from . import VAD
from multiprocessing import Pool

'''
New since version 2025.10.2
从version==2025.10.2开始，替代Reg_Step_Wise_MP成为rascpy内置的双向逐步回归模型。
与Reg_Step_Wise_MP相比，大幅缩短了计算时长。Reg_Step_Wise_MP中一个算法步骤可能会以一个极小的概率对模型有一个微弱的提升，但是却需要耗费大量运算时间。在StepwiseRegressionSKLearn中省去了这个步骤，因此计算时长得到了缩减。

它是python实现的线性双向逐步回归和逻辑双向逐步回归，比传统双向逐步回归增加以下功能：
从Reg_Step_Wise_MP保留的功能有：
1.逻辑回归逐步变量选择时，可以选择AUC、KS、LIFT指标替代AIC、BIC指标。对于一些业务，AUC、KS是更符合业务场景的指标。比如排序业务时，使用KS指标构建的模型，据以往经验，有使用变量更少，但在多个测试集上模型KS不下降的优点。
2.逐步变量选择时，支持用其他数据集计算模型评价指标，而非使用建模数据集。尤其当数据量较大，除训练集和测试集外还有验证集时，建议使用验证集计算评价指标来指导变量选择。这有助于降低过拟合。
3.支持使用部分数据计算模型评价指标来指导变量选择。场景举例：业务需要保持一定通过率N%，那么让前N%样本的坏事件发生率最低即可，无需全部样本参与计算。据以往经验：在合适场景下，用部分数据做评价指标选出的变量比用全部数据选出的变量少，但是用户关注的该指标在多个测试集上不下降。因为模型只关注头部更容易区分的样本点，无需过多变量即可完成业务目标。
4.支持设置多个条件，变量需要同时满足全部条件才可入模，将变量选择和模型诊断同步进行，避免模型诊断不通过导致反复建模。内置条件有：P-Value，VIF，相关系数，系数符号。
5.支持指定必须入模的变量。如果指定入模变量与第4点中的条件冲突，设计了完善的机制来解决。
6.建模过程输出到EXCEL，记录每个变量的删除原因和每一轮逐步回归的过程信息。

在version==2025.10.2中新添加的功能有：
7.支持用户指定每个变量组中可以入模变量的个数
8.新增sklearn接口，可以在sklearn的pipline中使用

'''

class _Regression():
    def __init__(self,y_label=None,user_save_cols=[],user_set_cols=[],measure=None,measure_frac=1
                 ,pvalue_max=0.01,vif_max=3,corr_max=0.6,coef_sign={},default_coef_sign=None
                 ,X_group_format=None,cnt_in_group={},default_cnt_in_group=None,fea_cnt=15,results_save=None):
        #,n_jobs=-1
        self.y_label = y_label
        self.user_save_cols = user_save_cols
        self.user_set_cols = user_set_cols
        self.measure = measure
        self.measure_frac = measure_frac
        self.pvalue_max = pvalue_max
        self.vif_max = vif_max
        self.corr_max = corr_max
        self.coef_sign = coef_sign
        self.default_coef_sign = default_coef_sign
        self.X_group_format = X_group_format
        if self.X_group_format is not None:
            self.gsplit,self.gindex = get_gsplit_gindex(self.X_group_format)  
        self.cnt_in_group = cnt_in_group
        self.default_cnt_in_group = default_cnt_in_group
        self.fea_cnt = fea_cnt
        
        # if n_jobs is None:
        #     self.n_jobs = os.cpu_count()
        # elif n_jobs < 0:
        #     self.n_jobs = os.cpu_count() - n_jobs
        # else:
        #     self.n_jobs = n_jobs
        
        self.results_save = results_save
        
    def _set_cols(self,X,y,sample_weight,fit_args,out_vars):
        records=[]
        record=pd.Series()
        record[lan['Round']]=1
        record[lan['Description of the round']] = lan['0082']
        records.append(record)
        estimator_ = self._fit(X,y,sample_weight,fit_args)
        estimator_stand = self._fit(X,y,sample_weight,fit_args,True)
        step_proc = pd.DataFrame(records).set_index(lan['Round'])
        estimator_perf,estimator_coef = self._estimator_summ(estimator_,estimator_stand)
        # '删除原因'
        del_reasons=pd.Series({ov:[lan['0108']] for ov in out_vars},name=lan['0109'])
        self._report(estimator_perf,estimator_coef,del_reasons,step_proc)
        return self.user_set_cols,estimator_,estimator_perf,estimator_coef,del_reasons,step_proc    
    
    def _perf(self,estimator_,X_val,y_val,sample_weight_val,val_args):
        if self.measure == 'aic':
            perf = estimator_.aic*-1
        elif self.measure == 'bic':
            perf = estimator_.bic*-1
        else:
            y_hat=estimator_.predict(sm.add_constant(X_val))
            
            if self.measure_frac is None or self.measure_frac==1:
                n = None
            elif np.abs(self.measure_frac)<1:
                n=int(np.around(y_hat.shape[0]*self.measure_frac,decimals=0))
            else:
                n = self.measure_frac 
            if n is not None:
                if n>=0:
                    y_hat = y_hat.sort_values(ascending=False)[0:n]
                else:
                    y_hat = y_hat.sort_values(ascending=False)[n:]
            y_true = y_val.loc[y_hat.index]
            
            perf = SCORERS[self.measure](y_true,y_hat,sample_weight=sample_weight_val,**val_args)
            perf = np.around(perf,4)
        return perf
    
    def _check_perf(self,curr_perf,estimator_,X_val,y_val,sample_weight_val,val_args):
        perf = self._perf(estimator_,X_val,y_val,sample_weight_val,val_args)
        return perf > curr_perf,perf
        
    def _check_sign(self,estimator_):
        check_sign = True
        if len(self.coef_sign)==0:
            return check_sign
        if len(self.coef_pos)>0:
            check_sign = (estimator_.params[estimator_.params.index.isin(self.coef_pos) & (~estimator_.params.index.isin(self.coef_incorret_cols))] > 0).all()
        if check_sign==True:
            if len(self.coef_neg) > 0:
                check_sign = (estimator_.params[estimator_.params.index.isin(self.coef_neg) & (~estimator_.params.index.isin(self.coef_incorret_cols))] < 0).all()  
        return check_sign
   
    def _check_pvalue(self,estimator_):
        if self.pvalue_max is None:
            return True
        check_pvalue = (estimator_.pvalues[(~estimator_.pvalues.index.isin(self.given_large_pvalue_cols)) & (estimator_.pvalues.index!='const')] <= self.pvalue_max).all()
        return check_pvalue
        
    def _check_group(self,estimator_):        
        if self.X_group_format is None:
            return True
        if len(self.cnt_in_group)==0:
            return True
        Dg_cnt={}
        cols = [i for i in _estimator_cols(estimator_)]
        for i in cols:
            g = parse_x_group(i,self.gsplit,self.gindex)
            if g is not None and g in self.cnt_in_group:
                Dg_cnt[g] = Dg_cnt.get(g,0) + 1
                if Dg_cnt[g] > self.cnt_in_group[g]:
                    return False
        return True
                
    def _check_vif(self,X):
        if self.vif_max is None:
            return True,None
        if X.shape[1] <2:
            return True,0

        vif = VIF(X)
        vif = vif.loc[~vif.index.isin(self.given_large_vif_cols)]
        vif_max = vif['VIF Factor'].max()
        check_vif = vif_max <= self.vif_max
        return check_vif,vif_max
       
    def _check_corr(self,X):
        if self.corr_max is None:
            return True,None
        if X.shape[1] <2:
            return True,0
        if X.shape[1] == len(self.user_save_cols):
            return True,None
        
        df_corr = X.corr()
        t = np.arange(df_corr.shape[1])
        df_corr.values[t,t] = np.nan
        df_corr = df_corr.loc[:,~df_corr.columns.isin(self.user_save_cols)]
        corr_max = np.around(df_corr.max().max(),4)
        check_corr = corr_max <= self.corr_max
        return check_corr,corr_max
        
    def _check(self,curr_perf,estimator_,X,X_val, y_val, sample_weight_val,val_args,check_all=False):
        Dcheck={}
    
        check_sign = self._check_sign(estimator_)
        Dcheck['check_sign'] = check_sign
        if check_sign == False and check_all==False:
            return Dcheck
        
        check_pvalue = self._check_pvalue(estimator_)
        Dcheck['check_pvalue'] = check_pvalue
        if check_pvalue == False and check_all==False:
            return Dcheck  
        
        check_group = self._check_group(estimator_)
        Dcheck['check_group'] = check_group
        if check_group == False and check_all==False:
            return Dcheck
        
        check_perf,perf = self._check_perf(curr_perf,estimator_,X_val,y_val,sample_weight_val,val_args)
        Dcheck['check_perf'] = check_perf
        Dcheck['perf']=perf
        if check_perf==False and check_all==False:
            return Dcheck
        
        check_vif,vif_max = self._check_vif(X)
        Dcheck['check_vif'] = check_vif
        Dcheck['vif_max'] = vif_max
        if check_vif == False and check_all==False:
            return Dcheck
        
        check_corr,corr_max = self._check_corr(X)
        Dcheck['check_corr'] = check_corr
        Dcheck['corr_max'] = corr_max
        if check_corr == False and check_all==False:
            return Dcheck
        return Dcheck
      
    # 将self.default_coef_sign添加到self.coef_sign
    # 所有正号变量和负号变量都已经放入list    
    def _get_coef_pos_neg(self,cols):
        self.coef_pos = []
        self.coef_neg = []
        for i in cols:
            if i not in self.coef_sign and self.default_coef_sign is not None:
                self.coef_sign[i] = self.default_coef_sign
        self.coef_pos = [k for k, v in self.coef_sign.items() if v == '+']
        self.coef_neg = [k for k, v in self.coef_sign.items() if v == '-']
    
    # 将self.default_cnt_in_group 合并进self.cnt_in_group,后续使用self.cnt_in_group即可
    def _update_cnt_in_group(self,cols):
        if self.X_group_format is None or self.default_cnt_in_group is None:
            return
        for i in cols:
            g = parse_x_group(i,self.gsplit,self.gindex)
            if g is not None and g not in self.cnt_in_group:
                self.cnt_in_group[g] = self.default_cnt_in_group  

    # 将有冲突的列都存入self.given_large_vif_cols，self.given_large_pvalue_cols，self.coef_incorret_cols
    # 如果指定变量超出self.cnt_in_group，则更新self.cnt_in_group
    def _save_cols_conflict(self,X,y,sample_weight,fit_args,X_val,y_val,sample_weight_val,val_args):
        self.given_large_vif_cols = []
        self.given_large_pvalue_cols = []
        self.coef_incorret_cols = []
        if len(self.user_save_cols)==0:
            return [],-np.inf
        try:
            user_save_cols_estimator_ = self._fit(X,y,sample_weight,fit_args)
            
            if self.vif_max is not None:
                given_large_vif_cols = VIF(X)
                given_large_vif_cols = given_large_vif_cols['VIF Factor'].apply(np.around,decimals=4)
                #如果user_save_cols变量之间的vif已经超出阈值，那么不影响其他变量引入。
                #如果是新引入的变量导致user_save_cols之中的变量的VIF从小于阈值变成大于阈值，则阻止该变量引入
                self.given_large_vif_cols = list(given_large_vif_cols.loc[given_large_vif_cols>self.vif_max].index)
                          
            if self.pvalue_max is not None:
                given_large_pvalues = user_save_cols_estimator_.pvalues[user_save_cols_estimator_.pvalues.index!='const'] 
                self.given_large_pvalue_cols = list(given_large_pvalues[given_large_pvalues > self.pvalue_max].index)
               
            if self.coef_sign is not None and len(self.coef_sign)>0:
                for i in user_save_cols_estimator_.params.index:
                    sign = self.coef_sign.get(i,None)
                    if sign is None:
                        continue
                    if sign == '+' and user_save_cols_estimator_.params[i]<0:
                        #如果设置了user_save_cols，但是sign一开始就不符合指定值的col会被记录在这里
                        self.coef_incorret_cols.append(i)
                    elif sign == '-' and user_save_cols_estimator_.params[i]>0:
                        self.coef_incorret_cols.append(i)
         
            if self.X_group_format is not None:            
                Dg_cnt={}
                if len(self.cnt_in_group)>0:
                    for i in self.user_save_cols:
                        g = parse_x_group(i,self.gsplit,self.gindex)
                        if g is not None and g in self.cnt_in_group:
                            g_cnt = Dg_cnt.get(g,0)
                            Dg_cnt[g] = g_cnt+1
                            if Dg_cnt[g] > self.cnt_in_group[g]:
                                self.cnt_in_group[g] = Dg_cnt[g]  
        except Exception as e:
            # 'rascpy:设置了保留变量：%s。但是在进行保留变量初始校验时发生错误'
            e.add_note(lan['1083']%self.user_save_cols)
            raise e 
        return self.user_save_cols.copy(),self._perf(user_save_cols_estimator_,X_val,y_val,sample_weight_val,val_args) 
    
    @staticmethod
    def _estimator_summ(estimator_,estimator_stand):
        summ = estimator_.summary2()
        estimator_perf = summ.tables[0]
        estimator_coef = summ.tables[1]
        estimator_coef = pd.concat([estimator_coef,estimator_stand.params],axis=1)
        estimator_coef = estimator_coef.rename({0:'Standardized Coefficients','z':'Wald','P>|z|':'Wald P-Values','P>|t|':'t P-Values'},axis=1).apply(np.around,decimals=4)
        return estimator_perf,estimator_coef
    
    def _report(self,estimator_perf,estimator_coef,del_reasons,step_proc):
        if self.results_save is not None:
            with pd.ExcelWriter(self.results_save) as writer:
                row_num=2
                # '回归模型'
                estimator_perf.to_excel(writer, sheet_name=lan['Model Info'],header=False,index=False,startrow=row_num)
                row_num = row_num+estimator_perf.shape[0]+4
                estimator_coef.to_excel(writer, sheet_name=lan['Model Info'],startrow=row_num)
                row_num = row_num+estimator_coef.shape[0]+4
                del_reasons.to_excel(writer, sheet_name=lan['Model Info'],startrow = row_num)
                row_num = row_num+del_reasons.shape[0]+4
                step_proc.to_excel(writer, sheet_name=lan['Model Info'],startrow = row_num) 
                
                            
    def _add_one_var(self,curr_perf,X,y,sample_weight,fit_args,X_val,y_val,sample_weight_val,val_args):
        try:
            estimator_ = self._fit(X,y,sample_weight,fit_args)
            Dcheck = self._check(curr_perf,estimator_,X,X_val, y_val, sample_weight_val,val_args)
            for k,v in Dcheck.items():
                if k.startswith('check_'):
                    if v == False:
                        return None           
            return Dcheck['perf']                      
        except Exception as e:
            # 'rascpy:在计算逐步回归向前操作时发生错误，尝试变量组合：%s，尝试加入列：%s'
            e.add_note(lan['1074']%(X.columns,X.columns[-1]))
            raise e     
        
 
    def _add_var(self,curr_perf,in_vars,out_vars,X,y,sample_weight,fit_args,X_val,y_val,sample_weight_val,val_args):
        results  = [(i,self._add_one_var(curr_perf,X[in_vars+[i]],y,sample_weight,fit_args,X_val[in_vars+[i]],y_val,sample_weight_val,val_args)) for i in out_vars]
        # if self.n_jobs == 1 or len(out_vars) < 2:
        #     results  = [(i,self._add_one_var(curr_perf,X[in_vars+[i]],y,sample_weight,fit_args,X_val[in_vars+[i]],y_val,sample_weight_val,val_args)) for i in out_vars]
        # elif self.n_jobs > 1:
        #     with Pool(min(self.n_jobs,len(out_vars))) as pool:
        #         results = [pool.apply_async(self._add_one_var,args = (curr_perf,X[in_vars+[i]],y,sample_weight,fit_args,X_val[in_vars+[i]],y_val,sample_weight_val,val_args)) for i in out_vars]
        #         results = [(i,result.get()) for i, result in zip(out_vars,results)]
        results = list(filter(lambda x:x[1] is not None,results))        
        if len(results) == 0:
            return None,None
        else:
            return sorted(results, key=lambda x:x[1])[-1]
 
    def _rm_one_var(self,curr_perf,to_col,X,y,sample_weight,fit_args,X_val,y_val,sample_weight_val,val_args):
        try:
            estimator_ = self._fit(X,y,sample_weight,fit_args)
            Dcheck = self._check(curr_perf,estimator_,X,X_val, y_val, sample_weight_val,val_args)
            for k,v in Dcheck.items():
                if k.startswith('check_'):
                    if v == False:
                        return None
            return Dcheck['perf']                               
        except Exception as e:
            # 'rascpy:在计算逐步回归向后操作时发生错误，尝试变量组合：%s,尝试去掉的列：%s'
            e.add_note(lan['1075']%(X.columns,to_col))
            raise e
                    
    def _rm_var(self,curr_perf,X,y,sample_weight,fit_args,X_val,y_val,sample_weight_val,val_args):
        cols = [i for i in X.columns if i not in self.user_save_cols]
        results  = [(to_col,self._rm_one_var(curr_perf,to_col,X[list(set(X.columns)-{to_col})],y,sample_weight,fit_args,X_val[list(set(X.columns)-{to_col})],y_val,sample_weight_val,val_args)) for to_col in cols]
        # if self.n_jobs == 1 or len(cols) < 2:
        #    results  = [(to_col,self._rm_one_var(curr_perf,to_col,X[list(set(X.columns)-{to_col})],y,sample_weight,fit_args,X_val[list(set(X.columns)-{to_col})],y_val,sample_weight_val,val_args)) for to_col in cols]
        # elif self.n_jobs > 1:   
        #     with Pool(min(self.n_jobs,len(cols))) as pool:
        #         results = [pool.apply_async(self._rm_one_var,args = (curr_perf,to_col,X[list(set(X.columns)-{to_col})],y,sample_weight,fit_args,X_val[list(set(X.columns)-{to_col})],y_val,sample_weight_val,val_args)) for to_col in cols]
        #         results = [(i,result.get()) for i,result in zip(cols,results)]
            
        results = list(filter(lambda x:x[1] is not None,results))
        if len(results) == 0:
            return None,None
        else:
            return sorted(results, key=lambda x:x[1])[-1]

    def _del_one_reasons(self,curr_perf,to_col,in_vars,X,y,sample_weight,fit_args,X_val,y_val,sample_weight_val,val_args):
        cols = [to_col]
        cols.extend(in_vars)
        X1 = X[cols]
        X_val1 = X_val[cols]       
        try:
            estimator_ = self._fit(X1,y,sample_weight,fit_args)
            Dcheck = self._check(curr_perf,estimator_,X1,X_val1, y_val, sample_weight_val,val_args,True)
        except Exception as e:
            # '在计算变量%s的删除原因时发生错误。入模变量为：%s'
            e.add_note(lan['0110']%(to_col,in_vars))
            raise e
            
        reasons = []
        if not Dcheck['check_perf']:
            if self.measure in ['aic','bic']:
                reasons.append(lan['0076']%(self.measure,Dcheck['perf']*-1,curr_perf*-1))
            else:
                reasons.append(lan['0077']%(self.measure,Dcheck['perf'],curr_perf))
                
        if not Dcheck['check_pvalue']: 
            reasons.append(lan['0080']%(self.pvalue_max))
            
        if not Dcheck['check_sign'] :
            reasons.append(lan['0081'])
            
        if not Dcheck['check_group']:
            reasons.append(lan['0154'])

        if not Dcheck['check_vif']:
            reasons.append(lan['0078']%(Dcheck['vif_max'],self.vif_max))

        if not Dcheck['check_corr']:
            reasons.append(lan['0079']%(Dcheck['corr_max'],self.corr_max))       
                             
        if len(reasons)==0:
            # 加入后模型指标提升，但由于iter_num达到了限制，所以没有加入模型。
            reasons.append(lan['0140'])
        return reasons
    
    def _del_reasons(self,curr_perf,in_vars,X,y,sample_weight,fit_args,X_val,y_val,sample_weight_val,val_args):
        #len(self.user_set_cols)>0 已经在_set_cols中处理
        out_vars = X.columns[~X.columns.isin(in_vars)]
        return {to_col:self._del_one_reasons(curr_perf,to_col,in_vars,X,y,sample_weight,fit_args,X_val,y_val,sample_weight_val,val_args) for to_col in out_vars}
        # if self.n_jobs == 1 or len(out_vars)<2:
        #     return {to_col:self._del_one_reasons(curr_perf,to_col,in_vars,X,y,sample_weight,fit_args,X_val,y_val,sample_weight_val,val_args) for to_col in out_vars}
                
        # elif self.n_jobs > 1:                
        #     with Pool(min(self.n_jobs,len(out_vars))) as pool:
        #         results = [pool.apply_async(self._del_one_reasons,args = (curr_perf,to_col,in_vars,X,y,sample_weight,fit_args,X_val,y_val,sample_weight_val,val_args)) for to_col in out_vars]
        #         return {to_col:result.get() for to_col,result in zip(out_vars,results)}
        
    def fit(self,X,y,sample_weight=None,fit_args={},X_val=None,y_val=None,sample_weight_val=None,val_args={}):
        '''
    训练模型

    Parameters
    ----------
    X : pandas.DataFrame
        用于模型训练的特征数据集
        
    y : pandas.Series
        用于模型训练的y标签
        
    sample_weight : pandas.Series, optional
        用于训练的样本权重
        None：每个样本权重相同
        默认：None.
        
    fit_args : dict, optional
        用于模型训练的其它参数
        默认：{}
        
    X_val : pandas.DataFrame, optional
        用于验证的特征数据集
        默认：None.
        
    y_val : pandas.Series, optional
        用于验证的y标签
        默认：None.
        
    sample_weight_val : pandas.Series, optional
        用于验证的样本权重
        None：每个样本权重相同
        默认：None.
        
    val_args : dict, optional
        用于模型评价的其它参数
        默认：{}

    Returns
    -------
    训练完成的StepwiseRegressionSKLearn.LogisticReg实例(self)
    训练完成的StepwiseRegressionSKLearn.LinearReg实例(self)   
    
    Attributes
    调用完fit后，StepwiseRegressionSKLearn.LogisticReg/LinearReg实例产生如下Attributes
    -------------------------------------------------------
    in_vars : list
       入模变量
    
    intercept_ : float       
    截距项
    
    coef_ : pandas.Series             
    各变量的系数（不含截距项）
             
    estimator_ :  statsmodels.regression.linear_model.RegressionResultsWrapper
                  / statsmodels.discrete.discrete_model.BinaryResultsWrapper
    部署线上应用时，如果线上python没有安装rascpy库，但是安装了statsmodels，那么用户可以直接使用estimator_ 进行模型部署
            
    perf : DataFrame
        模型构建信息：R-squared，调整R-squared，AIC，BIC，Log-Likelihood，F-statistic，Prob (F-statistic)等
            
    coef : DataFrame
        模型参数信息：Coef，Std.Err，系数检验t统计量，t统计量Pvalue，置信区间，Standardized Coefficients
                
    del_reasons : pandas.Series
        每个删除变量的删除原因
                
    step_proc : DataFrame
    每轮建模过程的详细记录，包括：添加或删除变量，模型的性能指标等。

        '''
        if X.shape[0] == 0 or X.shape[1]==0:
            print(lan['1178'])
            return None
        
        if self.user_set_cols is not None and len(self.user_set_cols) > 0:
            self.in_vars,self.estimator_,self.perf,self.coef,self.del_reasons,self.step_proc = self._set_cols(X[self.user_set_cols],y,sample_weight,fit_args,X.columns[~X.columns.isin(self.user_set_cols)])    
            self.intercept_=self.estimator_.params.const
            self.coef_=self.estimator_.params[1:]
            return self
                      
        if X_val is None:
            X_val = X
            y_val = y
        # 因为需要区分训练权重和评价权重，所以X_val为None时，sample_weight_val可能不为None
        # X_val为空并且sample_weight_val不为空，代表训练权重与评价权重是不同的
        if sample_weight_val is None:
            sample_weight_val = sample_weight
            
        self._get_coef_pos_neg(X.columns)
        self._update_cnt_in_group(X.columns)   
        in_vars,curr_perf = self._save_cols_conflict(X[self.user_save_cols],y,sample_weight,fit_args,X_val[self.user_save_cols],y_val,sample_weight_val,val_args)        
        records = []
        c=0      
        while(True):
            record=pd.Series()
            c+=1
            record[lan['Round']] = c
            if len(in_vars) >= self.fea_cnt:
                print(lan['0084']%(c,len(in_vars)))#'第%d轮：达到指定入模变量数量，建模结束。适当调大fea_cnt可能会有更好的模型效果'
                record[lan['Description of the round']]=lan['0085']%len(in_vars)# 达到指定入模变量数量，建模结束。适当调大iter_num可能会有更好的模型效果'
                records.append(record) 
                break 
            out_vars = X.columns[~X.columns.isin(in_vars)]   
            if len(out_vars) == 0:
                print(lan['0086']%(c,len(in_vars)))# '第%d轮：符合条件变量全部进入模型，建模结束'
                record[lan['Description of the round']]=lan['0087']%len(in_vars)# '符合条件变量全部进入模型，建模结束'
                records.append(record) 
                break 
            
            to_add_col,perf = self._add_var(curr_perf,in_vars,out_vars,X,y,sample_weight,fit_args,X_val,y_val,sample_weight_val,val_args)

            if to_add_col is not None:
                in_vars.append(to_add_col)
                curr_perf=perf 
                # lan['0088'] = '第%d轮：本轮增加变量%s'
                print(lan['0088']%(c,to_add_col))
                # '本轮增加变量'
                record[lan['0089']] = to_add_col
            elif to_add_col is None and len(in_vars)==0:
                # '第%d轮：没有变量能够进入模型，建模结束'
                print(lan['0092']%(c,len(in_vars)))
                # '没有变量能够进入模型，建模结束'
                record[lan['Description of the round']]=lan['0093']%len(in_vars)
                records.append(record) 
                break
            elif to_add_col is None: 
                # '第%d轮：在满足使用者所设置条件的前提下，已经不能通过增加或删除变量来进一步提升模型的指标，建模结束'
                print(lan['0097']%(c,len(in_vars)))
                # '在满足使用者所设置条件的前提下，已经不能通过增加或删除变量来进一步提升模型的指标，建模结束'
                record[lan['Description of the round']]=lan['0098']%len(in_vars)
                records.append(record) 
                break
            
            to_rm_col,perf = self._rm_var(curr_perf,X[in_vars],y,sample_weight,fit_args,X_val[in_vars],y_val,sample_weight_val,val_args)
                
            if to_rm_col is not None:
                in_vars.remove(to_rm_col)
                curr_perf=perf
                record[lan['0091']] = to_rm_col
                # '第%d轮：本轮删除变量%s'
                print(lan['0094']%(c,to_rm_col))
            
            if self.measure in ['aic','bic']:
                # '当前模型性能'
                record[lan['0099']]='%s = %s'%(self.measure,curr_perf*-1)
            else:
                record[lan['0099']]='%s = %s'%(self.measure,curr_perf)
            # '第%d轮：当前模型性能:%s'
            print(lan['0100']%(c,record[lan['0099']]))
            
            # '第%d轮：当前入模变量:%s'
            print(lan['0101']%(c,in_vars))
            # '当前入模变量'
            record[lan['0102']]=','.join(in_vars)
            
            if len(in_vars) == self.fea_cnt:
                # '第%d轮：到达指定轮次，建模结束。适当调大iter_num可能会有更好的模型效果'
                print(lan['0103']%(c,len(in_vars)))
                # '到达指定轮次，建模结束。适当调大iter_num可能会有更好的模型效果'
                record[lan['Description of the round']]=lan['0104']%len(in_vars)
                records.append(record) 
                break         
            elif len(X.columns[~X.columns.isin(in_vars)]) == 0:
                # '第%d轮：变量全部进入模型，建模结束'
                print(lan['0105']%(c,len(in_vars)))
                # '变量全部进入模型，建模结束'
                record[lan['Description of the round']]=lan['0106']%len(in_vars)
                records.append(record) 
                break
            else:
                # '第%d轮完成'
                print(lan['0107']%(c,len(in_vars)))
                # '第%d轮完成'
                record[lan['Description of the round']]=lan['0107']%(c,len(in_vars))
                records.append(record)  
            
        self.step_proc = pd.DataFrame(records).set_index(lan['Round'])
        self.estimator_ = self._fit(X[in_vars],y,sample_weight,fit_args,False)  
        estimator_stand = self._fit(X[in_vars],y,sample_weight,fit_args,True) 
        self.in_vars = in_vars
        curr_perf = self._perf(self.estimator_,X_val[self.in_vars],y_val,sample_weight_val,val_args)
        
        del_reasons = self._del_reasons(curr_perf,self.in_vars,X,y,sample_weight,fit_args,X_val,y_val,sample_weight_val,val_args)
        self.del_reasons = pd.Series(del_reasons,name=lan['0109'])
        self.perf,self.coef = self._estimator_summ(self.estimator_,estimator_stand)
        self._report(self.perf,self.coef,self.del_reasons,self.step_proc)
        self.intercept_=self.estimator_.params.const
        self.coef_=self.estimator_.params[1:]
        return self
            
import threading
import time
threads = threading.enumerate()
for thread in threads:
    if thread.name=='IPyInteractiveThread' and thread.daemon==True:
        TSDOXHTDSDFSRTHPM = 'StepwiseRegressionSKLearn'
if 'TSDOXHTDSDFSRTHPM' not in dir():
    print(lan['4150'])
    time.sleep(5)
    os._exit(status=1)
        
class LogisticReg(_Regression):
    def __init__(self,y_label={'unevent':0,'event':1},user_save_cols=[],user_set_cols=[],measure='roc_auc',measure_frac=1
                 ,pvalue_max=0.05,vif_max=3,corr_max=0.7,coef_sign={},default_coef_sign=None
                 ,X_group_format=None,cnt_in_group={},default_cnt_in_group=None,fea_cnt=15,results_save=None):
        # ,n_jobs=-1
        '''
    从version==2025.10.2开始，替代Reg_Step_Wise_MP.LogisticReg成为rascpy内置的双向逐步逻辑回归模型。Reg_Step_Wise_MP仍然保留，用户依然可以使用,但推荐使用StepwiseRegressionSKLearn.LogisticReg，因为计算时间大幅缩减。
    从Reg_Step_Wise_MP保留的功能：
    1.逻辑回归逐步变量选择时，可以选择AUC、KS、LIFT指标替代AIC、BIC指标。对于一些业务，AUC、KS是更符合业务场景的指标。比如排序业务时，使用KS指标构建的模型，据以往经验，有使用变量更少，但在多个测试集上模型KS不下降的优点。
    2.逐步变量选择时，支持用其他数据集计算模型评价指标，而非使用建模数据集。尤其当数据量较大，除训练集和测试集外还有验证集时，建议使用验证集计算评价指标来指导变量选择。这有助于降低过拟合。
    3.支持使用部分数据计算模型评价指标来指导变量选择。场景举例：业务需要保持一定通过率N%，那么让前N%样本的坏事件发生率最低即可，无需全部样本参与计算。据以往经验：在合适场景下，用部分数据做评价指标选出的变量比用全部数据选出的变量少，但是用户关注的该指标在多个测试集上不下降。因为模型只关注头部更容易区分的样本点，无需过多变量即可完成业务目标。
    4.支持设置多个条件，变量需要同时满足全部条件才可入模，将变量选择和模型诊断同步进行，避免模型诊断不通过导致反复建模。内置条件有：P-Value，VIF，相关系数，系数符号。
    5.支持指定必须入模的变量。如果指定入模变量与第4点中的条件冲突，设计了完善的机制来解决。
    6.建模过程输出到EXCEL，记录每个变量的删除原因和每一轮逐步回归的过程信息。

    New since version 2025.10.2
    7.支持用户指定每个变量组中可以入模的个数
    8.新增sklearn接口，可以在sklearn的pipline中使用
    

    Parameters
    ----------
    y_label : dict, optional
        将y中的哪个取值定义为事件发生，哪个取值定义为事件未发生。
        keys的取值只能是unevent或event
        values的取值要根据y的取值填写
        例：{'unevent':'good','event':'bad'}
        一般将用户最关心的事情定义为事件发生，这样解释起来更容易。比如：当想强调肺癌的发生，可以说吸烟的用户比不吸烟的用户肺癌发病率高50%，此时可以写成{'unevent':'没有肺癌','event':'肺癌'}，如果你写成{'unevent':'肺癌','event':'没有肺癌'}，尽管不影响模型的使用，但是解释的话术就要变成吸烟的用户比不吸烟的用户没有肺癌的发生率低50%，显然第一种表达方式更强调你所关注的事件。
        默认:{'unevent':0,'event':1}.
        
    user_save_cols : array like, optional
        强制入模的变量
        默认:[]
        
    user_set_cols : array like, optional
        只有这些变量能够入模，不增加也不删减。
        如果user_set_cols不为空并且长度大于0，逐步回归退化到普通回归。
        默认:[]
        
    measure : str, optional
        双向逐步回归时，判断模型是否有提升的指标。
        指标有：aic，bic，roc_auc，ks，lift_n(开发中)，ks_price(开发中)
        不能为None
        默认:'roc_auc'.
        
    measure_frac : float, optional
        按预测的事件发生概率从大到小或从小到大排序，从${MODEL CONFIG:measure_data_name}中取前N个样本点做模型的评价指标
        None：从${MODEL CONFIG:measure_data_name}取出全部样本点来计算模型的评价指标。等同于measure_frac=1。
        如果measure_index是aic或bic，则忽略measure_frac配置。只能使用全部建模数据
        measure_frac > 1：      从大到小取前 N = measure_frac 个样本点
        0 <measure_frac <= 1：  从大到小取前 N = sample_n*measure_frac 个样本点(向下取整)
        -1 <= measure_frac < 0：从小到大取前 N = sample_n*measure_frac*-1 个样本点(向下取整)
        measure_frac < -1：     从小到大取前 N = measure_frac*-1 个样本点
        默认:1
    
    pvalue_max : float, optional
        所有入模变量（不包含截距项）系数的p-value值必须小于等于该阈值
        使用者强制要求入模的变量不受此限制
        如果一个非强制入模变量入模后，引起了一个p-value原本小于阈值的强制入模变量的p-value超过阈值，则该非强制变量不会入模。但如果一个强制入模变量原本的p-value就超过阈值，即由其他强制入模变量导致的p-value超过阈值，则不影响该非强制入模变量的引入
        None：不对入模变量的p-value做约束
        默认:0.05 
        
    vif_max : float, optional
        所有入模变量（不包含截距项）的vif必须小于等于该阈值
        强制入模的变量不受此约束的影响
        如果一个非强制入模变量入模后，引起了一个vif原本小于阈值的强制入模变量的vif超过阈值，则该非强制变量不会入模。但如果一个强制入模变量本身的vif就超过阈值，即由其他强制入模变量导致的vif超过阈值，则不影响该非强制入模变量的引入
        None：不对入模变量的vif做限制
        默认:3
        
    corr_max : float, optional
        所有入模变量两两之间相关系数必须小于等于该阈值
        如果一个非强制入模变量，与强制入模变量的相关系数超出阈值，非强制入模变量不会被引入模型。
        即使两个强制入模变量的相关系数高于此阈值，这两个变量也都会被引入
        None：不对入模变量的相关系数做限制
        默认:0.7
        
    coef_sign : dict, optional
         对变量系数的符号约束
         ex. {"x1":"+","x2":"-"} 或者 file://xx/xx.json 从文件中读取
         取值说明： 
             + 该变量的系数为正号
             - 该变量的系数为负号
             None 该变量不做系数符号的约束
         coef_sign = None：对所有变量的系数符号不做约束
         使用者强制要求入模的变量不会受此约束限制
         如果一个非强制入模变量的引入使得一个本来满足符号约束的强制入模变量不再满足符号约束，则该非强制入模变量不能入模。如果强制入模变量本身符号就不满足约束，则不影响该非强制入模变量的引入。
         默认: {}
         
    default_coef_sign : str, optional
        当变量不在coef_sign中，则该变量符号约束的默认值
        None：所有变量的默认值为None
        默认:None
        
    X_group_format : str, optional
        New in version 2025.10.2
        X变量中组的表达方式
        业务上，X有时可以按照组来进行分类管理。比如A数据服务公司提供的所有数据可以分成一组，B数据服务公司提供的所有变量可以分成另外一组。
        ex1. X_group_format = _g
        ex2. X_group_format = g$$
        取值说明： 
        一个字符必须是g且只能出现在首或尾，如果g出现在前面，代表组名为变量名的前缀，如果g出现在后面，代表组名为变量名的后缀。无法处理组名在变量名中间的情况
        其余字符是组的分隔符，是不包含字母g的字符串。依靠该分隔符将组名从变量名中分离出来
        例： 如果变量的命名格式为 x1_group1,则此处应该配置成 _g
             如果变量的命名格式为 group1##x1,则此处应该配置成 g##
        如果一个变量名不含有配置的分隔符，说明该变量不在任何一个组中，后续按组操作变量的指令将不会应用在这个变量上
        None:所有X都不需要分组
        默认:None

    cnt_in_group : dict, optional
        设置每个变量组内允许最大的入模变量数
        例:{"g1":1,"g2":2}
        默认:{} 即没有任何组会受到入模变量个数的限制
    
    default_cnt_in_group : int, optional
        如果一个变量组没有在cnt_group中设置，则其默认允许的最大入模变量数
        None:没有默认的最大入模变量限制，如果变量组没有出现在cnt_in_group，则对组内变量的入模数量没有限制
        默认:None
        
    fea_cnt : int, optional
        入模变量的个数
        每次逐步回归会有两个操作：
            1.从所有剩余变量中找出符合约束条件下，他的加入会使模型指标比当前提升，且提升最高的一个变量。将该变量引入模型
            2.从所有入模变量中找出符合约束条件下，他的剔除会使模型指标比当前提升，且提升最高的一个变量。将该变量剔除模型
        如果已经入模N个变量(N < fea_cnt),通过加入或删除变量都无法进一步提升模型的性能，则逐步回归提前终止
        默认:15
        
    results_save : str, optional
        记录建模过程的文件名。文件里除常见信息外，还记录了逐步回归的对变量选入和剔除的过程，还记录了变量删除的原因。
        None：不记录过程
        默认:None.

    Returns
    -------
    None.

        '''

        super().__init__(y_label,user_save_cols,user_set_cols,measure,measure_frac
                     ,pvalue_max,vif_max,corr_max,coef_sign,default_coef_sign
                     ,X_group_format,cnt_in_group,default_cnt_in_group,fea_cnt,results_save)#,n_jobs
        
    @staticmethod    
    def _fit(X,y,sample_weight=None,fit_args={},standardized=False):
        try:
            if standardized:
                X = X.apply(stats.zscore)
            log_reg = sm.Logit(y, sm.add_constant(X))
            estimator_ = log_reg.fit(disp=False,**fit_args)
        except Exception as e:
            e.add_note(lan['1111']%X.columns)
            raise e
        return estimator_
    
    
    def predict_proba(self,X):
        '''
    返回每个标签类别预测的概率。顺序为标签label的字典序

    Parameters
    ----------
    X : pd.DataFrame
        待预测的特征数据集

    Returns
    -------
    proba_hat : array-like of shape (n_samples, n_classes)
        每个标签类别预测的概率。顺序为标签label的字典序。
        例如：
        [
         [0.2,0.8],
         [0.6,0.4],
            ...
        ]

        '''
        proba_hat = np.asarray(list(self.estimator_.predict(sm.add_constant(X[list(self.estimator_.params[1:].index)])).apply(lambda hat:[1-hat,hat])))
        return proba_hat

        
class LinearReg(_Regression):
    
    def __init__(self,user_save_cols=[],user_set_cols=[],measure='r2',measure_frac=1
                 ,pvalue_max=0.05,vif_max=3,corr_max=0.7,coef_sign={},default_coef_sign=None
                 ,X_group_format=None,cnt_in_group={},default_cnt_in_group=None,fea_cnt=15,results_save=None):
        # ,n_jobs=-1
        '''
从version==2025.10.2开始，替代Reg_Step_Wise_MP.LinearReg成为rascpy内置的双向逐步线性回归模型。Reg_Step_Wise_MP仍然保留，用户依然可以使用,但推荐使用StepwiseRegressionSKLearn.LinearReg，因为计算时间大幅缩减。
从Reg_Step_Wise_MP保留的功能：
1.逐步变量选择时，支持用其他数据集计算模型评价指标，而非使用建模数据集。尤其当数据量较大，除训练集和测试集外还有验证集时，建议使用验证集计算评价指标来指导变量选择。这有助于降低过拟合。
2.支持设置多个条件，变量需要同时满足全部条件才可入模，将变量选择和模型诊断同步进行，避免模型诊断不通过导致反复建模。内置条件有：P-Value，VIF，相关系数，系数符号。
3.支持指定必须入模的变量。如果指定入模变量与第4点中的条件冲突，设计了完善的机制来解决。
4.建模过程输出到EXCEL，记录每个变量的删除原因和每一轮逐步回归的过程信息。

New since version 2025.10.2
5.支持用户指定每个变量组中可以入模的个数
6.新增sklearn接口，可以在sklearn的pipline中使用
        

    Parameters
    ----------
    user_save_cols : array like, optional
        强制入模的变量
        默认:[]
        
    user_set_cols : array like, optional
        只有这些变量能够入模，不增加也不删减。
        如果user_set_cols不为空并且长度大于0，逐步回归退化到普通回归。
        默认:[]
        
    measure : str, optional
        双向逐步回归时，判断模型是否有提升的指标。
        指标有：r2
        默认:'r2'.
        
    measure_frac : float, optional
        按预测值从大到小或从小到大排序，从${MODEL CONFIG:measure_data_name}中取前N个样本点做模型的评价指标
        None：从${MODEL CONFIG:measure_data_name}取出全部样本点来计算模型的评价指标。等同于measure_frac=1。
        measure_frac > 1：      从大到小取前 N = measure_frac 个样本点
        0 <measure_frac <= 1：  从大到小取前 N = sample_n*measure_frac 个样本点(向下取整)
        -1 <= measure_frac < 0：从小到大取前 N = sample_n*measure_frac*-1 个样本点(向下取整)
        measure_frac < -1：     从小到大取前 N = measure_frac*-1 个样本点
        默认:1
    
    pvalue_max : float, optional
        所有入模变量（不包含截距项）系数的p-value值必须小于等于该阈值
        使用者强制要求入模的变量不受此限制
        如果一个非强制入模变量入模后，引起了一个p-value原本小于阈值的强制入模变量的p-value超过阈值，则该非强制变量不会入模。但如果一个强制入模变量原本的p-value就超过阈值，即由其他强制入模变量导致的p-value超过阈值，则不影响该非强制入模变量的引入
        None：不对入模变量的p-value做约束
        默认:0.05 
        
    vif_max : float, optional
        所有入模变量（不包含截距项）的vif必须小于等于该阈值
        强制入模的变量不受此约束的影响
        如果一个非强制入模变量入模后，引起了一个vif原本小于阈值的强制入模变量的vif超过阈值，则该非强制变量不会入模。但如果一个强制入模变量本身的vif就超过阈值，即由其他强制入模变量导致的vif超过阈值，则不影响该非强制入模变量的引入
        None：不对入模变量的vif做限制
        默认:3
        
    corr_max : float, optional
        所有入模变量两两之间相关系数必须小于等于该阈值
        如果一个非强制入模变量，与强制入模变量的相关系数超出阈值，非强制入模变量不会被引入模型。
        即使两个强制入模变量的相关系数高于此阈值，这两个变量也都会被引入
        None：不对入模变量的相关系数做限制
        默认:0.7
        
    coef_sign : dict, optional
         对变量系数的符号约束
         ex. {"x1":"+","x2":"-"} 或者 file://xx/xx.json 从文件中读取
         取值说明： 
             + 该变量的系数为正号
             - 该变量的系数为负号
             None 该变量不做系数符号的约束
         coef_sign = None：对所有变量的系数符号不做约束
         使用者强制要求入模的变量不会受此约束限制
         如果一个非强制入模变量的引入使得一个本来满足符号约束的强制入模变量不再满足符号约束，则该非强制入模变量不能入模。如果强制入模变量本身符号就不满足约束，则不影响该非强制入模变量的引入。
         默认: {}
         
    default_coef_sign : str, optional
        当变量不在coef_sign中，则该变量符号约束的默认值
        None：所有变量的默认值为None
        默认:None
        
    X_group_format : str, optional
        New in version 2025.10.2
        X变量中组的表达方式
        业务上，X有时可以按照组来进行分类管理。比如A数据服务公司提供的所有数据可以分成一组，B数据服务公司提供的所有变量可以分成另外一组。
        ex1. X_group_format = _g
        ex2. X_group_format = g$$
        取值说明： 
        一个字符必须是g且只能出现在首或尾，如果g出现在前面，代表组名为变量名的前缀，如果g出现在后面，代表组名为变量名的后缀。无法处理组名在变量名中间的情况
        其余字符是组的分隔符，是不包含字母g的字符串。依靠该分隔符将组名从变量名中分离出来
        例： 如果变量的命名格式为 x1_group1,则此处应该配置成 _g
             如果变量的命名格式为 group1##x1,则此处应该配置成 g##
        如果一个变量名不含有配置的分隔符，说明该变量不在任何一个组中，后续按组操作变量的指令将不会应用在这个变量上
        None:所有X都不需要分组
        默认:None

    cnt_in_group : dict, optional
        设置每个变量组内允许最大的入模变量数
        例:{"g1":1,"g2":2}
        默认:{} 即没有任何组会受到入模变量个数的限制
    
    default_cnt_in_group : int, optional
        如果一个变量组没有在cnt_group中设置，则其默认允许的最大入模变量数
        None:没有默认的最大入模变量限制，如果变量组没有出现在cnt_in_group，则对组内变量的入模数量没有限制
        默认:None
        
    fea_cnt : int, optional
        入模变量的个数
        每次逐步回归会有两个操作：
            1.从所有剩余变量中找出符合约束条件下，他的加入会使模型指标比当前提升，且提升最高的一个变量。将该变量引入模型
            2.从所有入模变量中找出符合约束条件下，他的剔除会使模型指标比当前提升，且提升最高的一个变量。将该变量剔除模型
        如果已经入模N个变量(N < fea_cnt),通过加入或删除变量都无法进一步提升模型的性能，则逐步回归提前终止
        默认:15
        
    results_save : str, optional
        记录建模过程的文件名。文件里除常见信息外，还记录了逐步回归的对变量选入和剔除的过程，还记录了变量删除的原因。
        None：不记录过程
        默认:None.

    Returns
    -------
    None.

        '''

        super().__init__(None,user_save_cols,user_set_cols,measure,measure_frac
                     ,pvalue_max,vif_max,corr_max,coef_sign,default_coef_sign
                     ,X_group_format,cnt_in_group,default_cnt_in_group,fea_cnt,results_save)#,n_jobs
        
    @staticmethod    
    def _fit(X,y,sample_weight=None,fit_args={},standardized=False):
        try:
            if standardized:
                X = X.apply(stats.zscore)
            if sample_weight is None:
                reg = sm.OLS(y,sm.add_constant(X))
            else:
                reg = sm.WLS(y,sm.add_constant(X),weights=sample_weight)
            estimator_ = reg.fit(disp=False,**fit_args)
            # estimator_.intercept_=estimator_.params.const
            # estimator_.coef_=estimator_.params[1:]
            # if adapte_sklearn_predict == True:
            #     estimator_.predict0 = estimator_.predict
            #     estimator_.predict=lambda D: np.asarray(list(estimator_.predict0(sm.add_constant(D[list(estimator_.params[1:].index)]))))
        except Exception as e:
            e.add_note(lan['1112']%X.columns)
            raise e
        return estimator_
    
    def predict(self,X):
        '''
    返回每个样本点的预测值

    Parameters
    ----------
    X : pd.DataFrame
        待预测的特征数据集

    Returns
    -------
    hat : array, shape (n_samples,)
        预测值

        '''
        return np.asarray(list(self.estimator_.predict(sm.add_constant(X[list(self.estimator_.params[1:].index)]))))
     
def _estimator_cols(estimator_):
    if hasattr(estimator_, 'coef_'):
        return list(estimator_.coef_.index)
    else:
        return list(estimator_.params[1:].index)    