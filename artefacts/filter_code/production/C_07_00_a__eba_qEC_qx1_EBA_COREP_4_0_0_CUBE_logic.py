from pybirdai.models.bird_data_model import *
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.process_steps.pybird.csv_converter import CSVConverter
from datetime import datetime
from pybirdai.annotations.decorators import lineage, track_table_init

class C_07_00_a__eba_qEC_qx1_EBA_COREP_4_0_0_CUBE_UnionItem:
	base = None #C_07_00_a__eba_qEC_qx1_EBA_COREP_4_0_0_CUBE_Base
	@lineage(dependencies={"base.ACCOUNTING_ITEMS"})
	def ACCOUNTING_ITEMS(self) -> str:
		''' return string from ACCOUNTING_ITEMS enumeration '''
		return self.base.ACCOUNTING_ITEMS()
	@lineage(dependencies={"base.ACCOUNTING_ITEMS_USED_AS_COLLATERAL_OR_GUARANTEE_RECEIVED"})
	def ACCOUNTING_ITEMS_USED_AS_COLLATERAL_OR_GUARANTEE_RECEIVED(self) -> str:
		''' return string from ACCOUNTING_ITEMS_USED_AS_COLLATERAL_OR_GUARANTEE_RECEIVED enumeration '''
		return self.base.ACCOUNTING_ITEMS_USED_AS_COLLATERAL_OR_GUARANTEE_RECEIVED()
	@lineage(dependencies={"base.APPLICABLE_CAPITAL_REGULATORY_REQUIREMENT"})
	def APPLICABLE_CAPITAL_REGULATORY_REQUIREMENT(self) -> str:
		''' return string from APPLICABLE_CAPITAL_REGULATORY_REQUIREMENT enumeration '''
		return self.base.APPLICABLE_CAPITAL_REGULATORY_REQUIREMENT()
	@lineage(dependencies={"base.APPROACH_FOR_DETERMINATION_OF_CCF"})
	def APPROACH_FOR_DETERMINATION_OF_CCF(self) -> str:
		''' return string from APPROACH_FOR_DETERMINATION_OF_CCF enumeration '''
		return self.base.APPROACH_FOR_DETERMINATION_OF_CCF()
	@lineage(dependencies={"base.BASE"})
	def BASE(self) -> str:
		''' return string from BASE enumeration '''
		return self.base.BASE()
	@lineage(dependencies={"base.CALCULATION_METHOD"})
	def CALCULATION_METHOD(self) -> str:
		''' return string from CALCULATION_METHOD enumeration '''
		return self.base.CALCULATION_METHOD()
	@lineage(dependencies={"base.CLLTRL_RL_TYP"})
	def CLLTRL_RL_TYP(self) -> str:
		''' return string from CLLTRL_RL_TYP enumeration '''
		return self.base.CLLTRL_RL_TYP()
	@lineage(dependencies={"base.CONVERSION_FACTORS_FOR_OFF_BALANCE_SHEET_ITEMS"})
	def CONVERSION_FACTORS_FOR_OFF_BALANCE_SHEET_ITEMS(self) -> str:
		''' return string from CONVERSION_FACTORS_FOR_OFF_BALANCE_SHEET_ITEMS enumeration '''
		return self.base.CONVERSION_FACTORS_FOR_OFF_BALANCE_SHEET_ITEMS()
	@lineage(dependencies={"base.COUNTERPARTY_NATURE"})
	def COUNTERPARTY_NATURE(self) -> str:
		''' return string from COUNTERPARTY_NATURE enumeration '''
		return self.base.COUNTERPARTY_NATURE()
	@lineage(dependencies={"base.CRM_EFFECTS_COLLATERAL"})
	def CRM_EFFECTS_COLLATERAL(self) -> str:
		''' return string from CRM_EFFECTS_COLLATERAL enumeration '''
		return self.base.CRM_EFFECTS_COLLATERAL()
	@lineage(dependencies={"base.EXPSR_CLSS"})
	def EXPSR_CLSS(self) -> str:
		''' return string from EXPSR_CLSS enumeration '''
		return self.base.EXPSR_CLSS()
	@lineage(dependencies={"base.FLOWS_DIRECTION"})
	def FLOWS_DIRECTION(self) -> str:
		''' return string from FLOWS_DIRECTION enumeration '''
		return self.base.FLOWS_DIRECTION()
	@lineage(dependencies={"base.IMPAIRMENT_STATUS"})
	def IMPAIRMENT_STATUS(self) -> str:
		''' return string from IMPAIRMENT_STATUS enumeration '''
		return self.base.IMPAIRMENT_STATUS()
	@lineage(dependencies={"base.METHODS_TO_DETERMINE_RISK_WEIGHTS"})
	def METHODS_TO_DETERMINE_RISK_WEIGHTS(self) -> str:
		''' return string from METHODS_TO_DETERMINE_RISK_WEIGHTS enumeration '''
		return self.base.METHODS_TO_DETERMINE_RISK_WEIGHTS()
	@lineage(dependencies={"base.OWN_FUNDS"})
	def OWN_FUNDS(self) -> str:
		''' return string from OWN_FUNDS enumeration '''
		return self.base.OWN_FUNDS()
	@lineage(dependencies={"base.OWN_FUNDS_CALCULATION_COMPONENT"})
	def OWN_FUNDS_CALCULATION_COMPONENT(self) -> str:
		''' return string from OWN_FUNDS_CALCULATION_COMPONENT enumeration '''
		return self.base.OWN_FUNDS_CALCULATION_COMPONENT()
	@lineage(dependencies={"base.PARTIAL_USE"})
	def PARTIAL_USE(self) -> str:
		''' return string from PARTIAL_USE enumeration '''
		return self.base.PARTIAL_USE()
	@lineage(dependencies={"base.PRUDENTIAL_APPROACH_THAT_AUTHORISED_BUT_NOT_APPLIED"})
	def PRUDENTIAL_APPROACH_THAT_AUTHORISED_BUT_NOT_APPLIED(self) -> str:
		''' return string from PRUDENTIAL_APPROACH_THAT_AUTHORISED_BUT_NOT_APPLIED enumeration '''
		return self.base.PRUDENTIAL_APPROACH_THAT_AUTHORISED_BUT_NOT_APPLIED()
	@lineage(dependencies={"base.PRUDENTIAL_PORTFOLIO"})
	def PRUDENTIAL_PORTFOLIO(self) -> str:
		''' return string from PRUDENTIAL_PORTFOLIO enumeration '''
		return self.base.PRUDENTIAL_PORTFOLIO()
	@lineage(dependencies={"base.REGULATORY_ADJUSTMENTS_INCLUDED_IN_THE_EXPOSURE"})
	def REGULATORY_ADJUSTMENTS_INCLUDED_IN_THE_EXPOSURE(self) -> str:
		''' return string from REGULATORY_ADJUSTMENTS_INCLUDED_IN_THE_EXPOSURE enumeration '''
		return self.base.REGULATORY_ADJUSTMENTS_INCLUDED_IN_THE_EXPOSURE()
	@lineage(dependencies={"base.REGULATORY_ASSESMENT_OF_TYPE_OF_ENTITY"})
	def REGULATORY_ASSESMENT_OF_TYPE_OF_ENTITY(self) -> str:
		''' return string from REGULATORY_ASSESMENT_OF_TYPE_OF_ENTITY enumeration '''
		return self.base.REGULATORY_ASSESMENT_OF_TYPE_OF_ENTITY()
	@lineage(dependencies={"base.RISK_WEIGHTS"})
	def RISK_WEIGHTS(self) -> str:
		''' return string from RISK_WEIGHTS enumeration '''
		return self.base.RISK_WEIGHTS()
	@lineage(dependencies={"base.SPECIFIC_CONTRACT_CLAUSES"})
	def SPECIFIC_CONTRACT_CLAUSES(self) -> str:
		''' return string from SPECIFIC_CONTRACT_CLAUSES enumeration '''
		return self.base.SPECIFIC_CONTRACT_CLAUSES()
	@lineage(dependencies={"base.TRANSITIONAL_PROVISIONS"})
	def TRANSITIONAL_PROVISIONS(self) -> str:
		''' return string from TRANSITIONAL_PROVISIONS enumeration '''
		return self.base.TRANSITIONAL_PROVISIONS()
	@lineage(dependencies={"base.TYPE_OF_ADJUSTMENT"})
	def TYPE_OF_ADJUSTMENT(self) -> str:
		''' return string from TYPE_OF_ADJUSTMENT enumeration '''
		return self.base.TYPE_OF_ADJUSTMENT()
	@lineage(dependencies={"base.TYPE_OF_CLEARING"})
	def TYPE_OF_CLEARING(self) -> str:
		''' return string from TYPE_OF_CLEARING enumeration '''
		return self.base.TYPE_OF_CLEARING()
	@lineage(dependencies={"base.TYPE_OF_CREDIT_RISK_MITIGATION"})
	def TYPE_OF_CREDIT_RISK_MITIGATION(self) -> str:
		''' return string from TYPE_OF_CREDIT_RISK_MITIGATION enumeration '''
		return self.base.TYPE_OF_CREDIT_RISK_MITIGATION()
	@lineage(dependencies={"base.TYPE_OF_FINANCIAL_INSTRUMENTS"})
	def TYPE_OF_FINANCIAL_INSTRUMENTS(self) -> str:
		''' return string from TYPE_OF_FINANCIAL_INSTRUMENTS enumeration '''
		return self.base.TYPE_OF_FINANCIAL_INSTRUMENTS()
	@lineage(dependencies={"base.TYPE_OF_FINANCIAL_INSTRUMENTS_USED_IN_CREDIT_RISK_MITIGATION"})
	def TYPE_OF_FINANCIAL_INSTRUMENTS_USED_IN_CREDIT_RISK_MITIGATION(self) -> str:
		''' return string from TYPE_OF_FINANCIAL_INSTRUMENTS_USED_IN_CREDIT_RISK_MITIGATION enumeration '''
		return self.base.TYPE_OF_FINANCIAL_INSTRUMENTS_USED_IN_CREDIT_RISK_MITIGATION()
	@lineage(dependencies={"base.TYPE_OF_RISK"})
	def TYPE_OF_RISK(self) -> str:
		''' return string from TYPE_OF_RISK enumeration '''
		return self.base.TYPE_OF_RISK()
	@lineage(dependencies={"base.USE_OF_EXTERNAL_RATINGS"})
	def USE_OF_EXTERNAL_RATINGS(self) -> str:
		''' return string from USE_OF_EXTERNAL_RATINGS enumeration '''
		return self.base.USE_OF_EXTERNAL_RATINGS()
	@lineage(dependencies={"base.ADJUSTMENTS_TO_THE_RISK_WEIGHTED_EXPOSURE_AMOUNT"})
	def ADJUSTMENTS_TO_THE_RISK_WEIGHTED_EXPOSURE_AMOUNT(self) -> str:
		''' return string from ADJUSTMENTS_TO_THE_RISK_WEIGHTED_EXPOSURE_AMOUNT enumeration '''
		return self.base.ADJUSTMENTS_TO_THE_RISK_WEIGHTED_EXPOSURE_AMOUNT()
	@lineage(dependencies={"base.AMOUNT_OF_CRM_SUBSTITUTION_EFFECTS"})
	def AMOUNT_OF_CRM_SUBSTITUTION_EFFECTS(self) -> str:
		''' return string from AMOUNT_OF_CRM_SUBSTITUTION_EFFECTS enumeration '''
		return self.base.AMOUNT_OF_CRM_SUBSTITUTION_EFFECTS()
	@lineage(dependencies={"base.CVAM_VOLATILITY_ADJUSTED_VALUE_OF_THE_COLLATERAL_CVA_FURTHER_ADJUSTED_FOR_MATURITY_MISMATCH"})
	def CVAM_VOLATILITY_ADJUSTED_VALUE_OF_THE_COLLATERAL_CVA_FURTHER_ADJUSTED_FOR_MATURITY_MISMATCH(self) -> str:
		''' return string from CVAM_VOLATILITY_ADJUSTED_VALUE_OF_THE_COLLATERAL_CVA_FURTHER_ADJUSTED_FOR_MATURITY_MISMATCH enumeration '''
		return self.base.CVAM_VOLATILITY_ADJUSTED_VALUE_OF_THE_COLLATERAL_CVA_FURTHER_ADJUSTED_FOR_MATURITY_MISMATCH()
	@lineage(dependencies={"base.EXPOSURE_VALUE"})
	def EXPOSURE_VALUE(self) -> str:
		''' return string from EXPOSURE_VALUE enumeration '''
		return self.base.EXPOSURE_VALUE()
	@lineage(dependencies={"base.FULLY_ADJUSTED_EXPOSURE_VALUE_E"})
	def FULLY_ADJUSTED_EXPOSURE_VALUE_E(self) -> str:
		''' return string from FULLY_ADJUSTED_EXPOSURE_VALUE_E enumeration '''
		return self.base.FULLY_ADJUSTED_EXPOSURE_VALUE_E()
	@lineage(dependencies={"base.FULLY_ADJUSTED_EXPOSURE_VALUE_E_NET_OF_VALUE_ADJUSTMENTS_AND_PROVISIONS"})
	def FULLY_ADJUSTED_EXPOSURE_VALUE_E_NET_OF_VALUE_ADJUSTMENTS_AND_PROVISIONS(self) -> str:
		''' return string from FULLY_ADJUSTED_EXPOSURE_VALUE_E_NET_OF_VALUE_ADJUSTMENTS_AND_PROVISIONS enumeration '''
		return self.base.FULLY_ADJUSTED_EXPOSURE_VALUE_E_NET_OF_VALUE_ADJUSTMENTS_AND_PROVISIONS()
	@lineage(dependencies={"base.ORIGINAL_EXPOSURE_PRE_CONVERSION_FACTORS"})
	def ORIGINAL_EXPOSURE_PRE_CONVERSION_FACTORS(self) -> str:
		''' return string from ORIGINAL_EXPOSURE_PRE_CONVERSION_FACTORS enumeration '''
		return self.base.ORIGINAL_EXPOSURE_PRE_CONVERSION_FACTORS()
	@lineage(dependencies={"base.RISK_WEIGHTED_EXPOSURE_AMOUNT"})
	def RISK_WEIGHTED_EXPOSURE_AMOUNT(self) -> str:
		''' return string from RISK_WEIGHTED_EXPOSURE_AMOUNT enumeration '''
		return self.base.RISK_WEIGHTED_EXPOSURE_AMOUNT()
	@lineage(dependencies={"base.VALUE_OF_ADJUSTMENTS_AND_PROVISION_ASSOCIATED_WITH_THE_ORIGINAL_EXPOSURE"})
	def VALUE_OF_ADJUSTMENTS_AND_PROVISION_ASSOCIATED_WITH_THE_ORIGINAL_EXPOSURE(self) -> str:
		''' return string from VALUE_OF_ADJUSTMENTS_AND_PROVISION_ASSOCIATED_WITH_THE_ORIGINAL_EXPOSURE enumeration '''
		return self.base.VALUE_OF_ADJUSTMENTS_AND_PROVISION_ASSOCIATED_WITH_THE_ORIGINAL_EXPOSURE()
	@lineage(dependencies={"base.VOLATILITY_ADJUSTMENT_TO_THE_EXPOSURE_EVA_E"})
	def VOLATILITY_ADJUSTMENT_TO_THE_EXPOSURE_EVA_E(self) -> str:
		''' return string from VOLATILITY_ADJUSTMENT_TO_THE_EXPOSURE_EVA_E enumeration '''
		return self.base.VOLATILITY_ADJUSTMENT_TO_THE_EXPOSURE_EVA_E()
	@lineage(dependencies={"base.VOLATILITY_AND_MATURITY_ADJUSTMENTS_TO_THE_EXPOSURE"})
	def VOLATILITY_AND_MATURITY_ADJUSTMENTS_TO_THE_EXPOSURE(self) -> str:
		''' return string from VOLATILITY_AND_MATURITY_ADJUSTMENTS_TO_THE_EXPOSURE enumeration '''
		return self.base.VOLATILITY_AND_MATURITY_ADJUSTMENTS_TO_THE_EXPOSURE()

class C_07_00_a__eba_qEC_qx1_EBA_COREP_4_0_0_CUBE_Base:
	def ACCOUNTING_ITEMS(self) -> str:
		''' return string from ACCOUNTING_ITEMS enumeration '''
		pass
	def ACCOUNTING_ITEMS_USED_AS_COLLATERAL_OR_GUARANTEE_RECEIVED(self) -> str:
		''' return string from ACCOUNTING_ITEMS_USED_AS_COLLATERAL_OR_GUARANTEE_RECEIVED enumeration '''
		pass
	def APPLICABLE_CAPITAL_REGULATORY_REQUIREMENT(self) -> str:
		''' return string from APPLICABLE_CAPITAL_REGULATORY_REQUIREMENT enumeration '''
		pass
	def APPROACH_FOR_DETERMINATION_OF_CCF(self) -> str:
		''' return string from APPROACH_FOR_DETERMINATION_OF_CCF enumeration '''
		pass
	def BASE(self) -> str:
		''' return string from BASE enumeration '''
		pass
	def CALCULATION_METHOD(self) -> str:
		''' return string from CALCULATION_METHOD enumeration '''
		pass
	def CLLTRL_RL_TYP(self) -> str:
		''' return string from CLLTRL_RL_TYP enumeration '''
		pass
	def CONVERSION_FACTORS_FOR_OFF_BALANCE_SHEET_ITEMS(self) -> str:
		''' return string from CONVERSION_FACTORS_FOR_OFF_BALANCE_SHEET_ITEMS enumeration '''
		pass
	def COUNTERPARTY_NATURE(self) -> str:
		''' return string from COUNTERPARTY_NATURE enumeration '''
		pass
	def CRM_EFFECTS_COLLATERAL(self) -> str:
		''' return string from CRM_EFFECTS_COLLATERAL enumeration '''
		pass
	def EXPSR_CLSS(self) -> str:
		''' return string from EXPSR_CLSS enumeration '''
		pass
	def FLOWS_DIRECTION(self) -> str:
		''' return string from FLOWS_DIRECTION enumeration '''
		pass
	def IMPAIRMENT_STATUS(self) -> str:
		''' return string from IMPAIRMENT_STATUS enumeration '''
		pass
	def METHODS_TO_DETERMINE_RISK_WEIGHTS(self) -> str:
		''' return string from METHODS_TO_DETERMINE_RISK_WEIGHTS enumeration '''
		pass
	def OWN_FUNDS(self) -> str:
		''' return string from OWN_FUNDS enumeration '''
		pass
	def OWN_FUNDS_CALCULATION_COMPONENT(self) -> str:
		''' return string from OWN_FUNDS_CALCULATION_COMPONENT enumeration '''
		pass
	def PARTIAL_USE(self) -> str:
		''' return string from PARTIAL_USE enumeration '''
		pass
	def PRUDENTIAL_APPROACH_THAT_AUTHORISED_BUT_NOT_APPLIED(self) -> str:
		''' return string from PRUDENTIAL_APPROACH_THAT_AUTHORISED_BUT_NOT_APPLIED enumeration '''
		pass
	def PRUDENTIAL_PORTFOLIO(self) -> str:
		''' return string from PRUDENTIAL_PORTFOLIO enumeration '''
		pass
	def REGULATORY_ADJUSTMENTS_INCLUDED_IN_THE_EXPOSURE(self) -> str:
		''' return string from REGULATORY_ADJUSTMENTS_INCLUDED_IN_THE_EXPOSURE enumeration '''
		pass
	def REGULATORY_ASSESMENT_OF_TYPE_OF_ENTITY(self) -> str:
		''' return string from REGULATORY_ASSESMENT_OF_TYPE_OF_ENTITY enumeration '''
		pass
	def RISK_WEIGHTS(self) -> str:
		''' return string from RISK_WEIGHTS enumeration '''
		pass
	def SPECIFIC_CONTRACT_CLAUSES(self) -> str:
		''' return string from SPECIFIC_CONTRACT_CLAUSES enumeration '''
		pass
	def TRANSITIONAL_PROVISIONS(self) -> str:
		''' return string from TRANSITIONAL_PROVISIONS enumeration '''
		pass
	def TYPE_OF_ADJUSTMENT(self) -> str:
		''' return string from TYPE_OF_ADJUSTMENT enumeration '''
		pass
	def TYPE_OF_CLEARING(self) -> str:
		''' return string from TYPE_OF_CLEARING enumeration '''
		pass
	def TYPE_OF_CREDIT_RISK_MITIGATION(self) -> str:
		''' return string from TYPE_OF_CREDIT_RISK_MITIGATION enumeration '''
		pass
	def TYPE_OF_FINANCIAL_INSTRUMENTS(self) -> str:
		''' return string from TYPE_OF_FINANCIAL_INSTRUMENTS enumeration '''
		pass
	def TYPE_OF_FINANCIAL_INSTRUMENTS_USED_IN_CREDIT_RISK_MITIGATION(self) -> str:
		''' return string from TYPE_OF_FINANCIAL_INSTRUMENTS_USED_IN_CREDIT_RISK_MITIGATION enumeration '''
		pass
	def TYPE_OF_RISK(self) -> str:
		''' return string from TYPE_OF_RISK enumeration '''
		pass
	def USE_OF_EXTERNAL_RATINGS(self) -> str:
		''' return string from USE_OF_EXTERNAL_RATINGS enumeration '''
		pass
	def ADJUSTMENTS_TO_THE_RISK_WEIGHTED_EXPOSURE_AMOUNT(self) -> str:
		''' return string from ADJUSTMENTS_TO_THE_RISK_WEIGHTED_EXPOSURE_AMOUNT enumeration '''
		pass
	def AMOUNT_OF_CRM_SUBSTITUTION_EFFECTS(self) -> str:
		''' return string from AMOUNT_OF_CRM_SUBSTITUTION_EFFECTS enumeration '''
		pass
	def CVAM_VOLATILITY_ADJUSTED_VALUE_OF_THE_COLLATERAL_CVA_FURTHER_ADJUSTED_FOR_MATURITY_MISMATCH(self) -> str:
		''' return string from CVAM_VOLATILITY_ADJUSTED_VALUE_OF_THE_COLLATERAL_CVA_FURTHER_ADJUSTED_FOR_MATURITY_MISMATCH enumeration '''
		pass
	def EXPOSURE_VALUE(self) -> str:
		''' return string from EXPOSURE_VALUE enumeration '''
		pass
	def FULLY_ADJUSTED_EXPOSURE_VALUE_E(self) -> str:
		''' return string from FULLY_ADJUSTED_EXPOSURE_VALUE_E enumeration '''
		pass
	def FULLY_ADJUSTED_EXPOSURE_VALUE_E_NET_OF_VALUE_ADJUSTMENTS_AND_PROVISIONS(self) -> str:
		''' return string from FULLY_ADJUSTED_EXPOSURE_VALUE_E_NET_OF_VALUE_ADJUSTMENTS_AND_PROVISIONS enumeration '''
		pass
	def ORIGINAL_EXPOSURE_PRE_CONVERSION_FACTORS(self) -> str:
		''' return string from ORIGINAL_EXPOSURE_PRE_CONVERSION_FACTORS enumeration '''
		pass
	def RISK_WEIGHTED_EXPOSURE_AMOUNT(self) -> str:
		''' return string from RISK_WEIGHTED_EXPOSURE_AMOUNT enumeration '''
		pass
	def VALUE_OF_ADJUSTMENTS_AND_PROVISION_ASSOCIATED_WITH_THE_ORIGINAL_EXPOSURE(self) -> str:
		''' return string from VALUE_OF_ADJUSTMENTS_AND_PROVISION_ASSOCIATED_WITH_THE_ORIGINAL_EXPOSURE enumeration '''
		pass
	def VOLATILITY_ADJUSTMENT_TO_THE_EXPOSURE_EVA_E(self) -> str:
		''' return string from VOLATILITY_ADJUSTMENT_TO_THE_EXPOSURE_EVA_E enumeration '''
		pass
	def VOLATILITY_AND_MATURITY_ADJUSTMENTS_TO_THE_EXPOSURE(self) -> str:
		''' return string from VOLATILITY_AND_MATURITY_ADJUSTMENTS_TO_THE_EXPOSURE enumeration '''
		pass

class C_07_00_a__eba_qEC_qx1_EBA_COREP_4_0_0_CUBE_UnionTable :
	C_07_00_a__eba_qEC_qx1_EBA_COREP_4_0_0_CUBE_UnionItems = [] # C_07_00_a__eba_qEC_qx1_EBA_COREP_4_0_0_CUBE_UnionItem []
	C_07_00_a__eba_qEC_qx1_EBA_COREP_4_0_0_CUBE_Credit_or_Counterparty_Risk_Exposure_Data_Table = None # Credit_or_Counterparty_Risk_Exposure_Data
	def calc_C_07_00_a__eba_qEC_qx1_EBA_COREP_4_0_0_CUBE_UnionItems(self) -> list[C_07_00_a__eba_qEC_qx1_EBA_COREP_4_0_0_CUBE_UnionItem] :
		items = [] # C_07_00_a__eba_qEC_qx1_EBA_COREP_4_0_0_CUBE_UnionItem []
		for item in self.C_07_00_a__eba_qEC_qx1_EBA_COREP_4_0_0_CUBE_Credit_or_Counterparty_Risk_Exposure_Data_Table.Credit_or_Counterparty_Risk_Exposure_Datas:
			newItem = C_07_00_a__eba_qEC_qx1_EBA_COREP_4_0_0_CUBE_UnionItem()
			newItem.base = item
			items.append(newItem)
		return items

	def init(self):
		Orchestration().init(self)
		self.C_07_00_a__eba_qEC_qx1_EBA_COREP_4_0_0_CUBE_UnionItems = []
		self.C_07_00_a__eba_qEC_qx1_EBA_COREP_4_0_0_CUBE_UnionItems.extend(self.calc_C_07_00_a__eba_qEC_qx1_EBA_COREP_4_0_0_CUBE_UnionItems())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class Credit_or_Counterparty_Risk_Exposure_Data(C_07_00_a__eba_qEC_qx1_EBA_COREP_4_0_0_CUBE_Base):
	CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT = None # CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.ACCOUNTING_ITEMS"})
	def ACCOUNTING_ITEMS(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.ACCOUNTING_ITEMS
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.ACCOUNTING_ITEMS_USED_AS_COLLATERAL_OR_GUARANTEE_RECEIVED"})
	def ACCOUNTING_ITEMS_USED_AS_COLLATERAL_OR_GUARANTEE_RECEIVED(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.ACCOUNTING_ITEMS_USED_AS_COLLATERAL_OR_GUARANTEE_RECEIVED
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.APPLICABLE_CAPITAL_REGULATORY_REQUIREMENT"})
	def APPLICABLE_CAPITAL_REGULATORY_REQUIREMENT(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.APPLICABLE_CAPITAL_REGULATORY_REQUIREMENT
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.APPROACH_FOR_DETERMINATION_OF_CCF"})
	def APPROACH_FOR_DETERMINATION_OF_CCF(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.APPROACH_FOR_DETERMINATION_OF_CCF
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.CALCULATION_METHOD"})
	def CALCULATION_METHOD(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.CALCULATION_METHOD
	def CLLTRL_RL_TYP(self):
		''' defaulty to 1 for now as we did not add it to the SQLDEveloper logic yet '''
		return '1'
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.CONVERSION_FACTORS_FOR_OFF_BALANCE_SHEET_ITEMS"})
	def CONVERSION_FACTORS_FOR_OFF_BALANCE_SHEET_ITEMS(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.CONVERSION_FACTORS_FOR_OFF_BALANCE_SHEET_ITEMS
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.COUNTERPARTY_NATURE"})
	def COUNTERPARTY_NATURE(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.COUNTERPARTY_NATURE
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.CRM_EFFECTS_COLLATERAL"})
	def CRM_EFFECTS_COLLATERAL(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.CRM_EFFECTS_COLLATERAL
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.FLOWS_DIRECTION"})
	def FLOWS_DIRECTION(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.FLOWS_DIRECTION
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.IMPAIRMENT_STATUS"})
	def IMPAIRMENT_STATUS(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.IMPAIRMENT_STATUS
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.METHODS_TO_DETERMINE_RISK_WEIGHTS"})
	def METHODS_TO_DETERMINE_RISK_WEIGHTS(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.METHODS_TO_DETERMINE_RISK_WEIGHTS
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.OWN_FUNDS_CALCULATION_COMPONENT"})
	def OWN_FUNDS_CALCULATION_COMPONENT(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.OWN_FUNDS_CALCULATION_COMPONENT
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.PARTIAL_USE"})
	def PARTIAL_USE(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.PARTIAL_USE
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.PRUDENTIAL_APPROACH_THAT_AUTHORISED_BUT_NOT_APPLIED"})
	def PRUDENTIAL_APPROACH_THAT_AUTHORISED_BUT_NOT_APPLIED(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.PRUDENTIAL_APPROACH_THAT_AUTHORISED_BUT_NOT_APPLIED
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.PRUDENTIAL_PORTFOLIO"})
	def PRUDENTIAL_PORTFOLIO(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.PRUDENTIAL_PORTFOLIO
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.REGULATORY_ADJUSTMENTS_INCLUDED_IN_THE_EXPOSURE"})
	def REGULATORY_ADJUSTMENTS_INCLUDED_IN_THE_EXPOSURE(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.REGULATORY_ADJUSTMENTS_INCLUDED_IN_THE_EXPOSURE
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.REGULATORY_ASSESMENT_OF_TYPE_OF_ENTITY"})
	def REGULATORY_ASSESMENT_OF_TYPE_OF_ENTITY(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.REGULATORY_ASSESMENT_OF_TYPE_OF_ENTITY
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.RISK_WEIGHTS"})
	def RISK_WEIGHTS(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.RISK_WEIGHTS
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.SPECIFIC_CONTRACT_CLAUSES"})
	def SPECIFIC_CONTRACT_CLAUSES(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.SPECIFIC_CONTRACT_CLAUSES
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.TRANSITIONAL_PROVISIONS"})
	def TRANSITIONAL_PROVISIONS(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.TRANSITIONAL_PROVISIONS
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.TYPE_OF_ADJUSTMENT"})
	def TYPE_OF_ADJUSTMENT(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.TYPE_OF_ADJUSTMENT
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.TYPE_OF_CLEARING"})
	def TYPE_OF_CLEARING(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.TYPE_OF_CLEARING
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.TYPE_OF_CREDIT_RISK_MITIGATION"})
	def TYPE_OF_CREDIT_RISK_MITIGATION(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.TYPE_OF_CREDIT_RISK_MITIGATION
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.TYPE_OF_FINANCIAL_INSTRUMENTS"})
	def TYPE_OF_FINANCIAL_INSTRUMENTS(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.TYPE_OF_FINANCIAL_INSTRUMENTS
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.TYPE_OF_FINANCIAL_INSTRUMENTS_USED_IN_CREDIT_RISK_MITIGATION"})
	def TYPE_OF_FINANCIAL_INSTRUMENTS_USED_IN_CREDIT_RISK_MITIGATION(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.TYPE_OF_FINANCIAL_INSTRUMENTS_USED_IN_CREDIT_RISK_MITIGATION
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.TYPE_OF_RISK"})
	def TYPE_OF_RISK(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.TYPE_OF_RISK
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.USE_OF_EXTERNAL_RATINGS"})
	def USE_OF_EXTERNAL_RATINGS(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.USE_OF_EXTERNAL_RATINGS
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.EXPOSURE_VALUE"})
	def EXPOSURE_VALUE(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.EXPOSURE_VALUE
	@lineage(dependencies={"CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.ORIGINAL_EXPOSURE_PRE_CONVERSION_FACTORS"})
	def ORIGINAL_EXPOSURE_PRE_CONVERSION_FACTORS(self):
		return self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT.ORIGINAL_EXPOSURE_PRE_CONVERSION_FACTORS

class C_07_00_a__eba_qEC_qx1_EBA_COREP_4_0_0_CUBE_Credit_or_Counterparty_Risk_Exposure_Data_Table:
	CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT_Table = None # CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT
	Credit_or_Counterparty_Risk_Exposure_Datas = []# Credit_or_Counterparty_Risk_Exposure_Data[]
	def calc_Credit_or_Counterparty_Risk_Exposure_Datas(self) :
		items = [] # Credit_or_Counterparty_Risk_Exposure_Data[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		for item in self.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT_Table:
			newItem = Credit_or_Counterparty_Risk_Exposure_Data()
			newItem.CNTRPRTY_OR_ISSR_EXPSR_RSK_EXPSR_DT = item
			newItem.base = item
			items.append(newItem)
		return items
	def init(self):
		Orchestration().init(self)
		self.Credit_or_Counterparty_Risk_Exposure_Datas = []
		self.Credit_or_Counterparty_Risk_Exposure_Datas.extend(self.calc_Credit_or_Counterparty_Risk_Exposure_Datas())
		CSVConverter.persist_object_as_csv(self,True)
		return None
