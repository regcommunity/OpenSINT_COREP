from pybirdai.models.bird_data_model import *
# Note: output_tables.py no longer needed - using direct product-specific classes
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.annotations.decorators import lineage

from .F_05_01_REF_FINREP_3_0_logic import *



class Cell_F_05_01_REF_FINREP_3_0_408956_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.GRSS_CRRYNG_AMNT", "Credit_card_debt.GRSS_CRRYNG_AMNT", "Trade_receivables.GRSS_CRRYNG_AMNT", "Advances_that_are_not_loans.GRSS_CRRYNG_AMNT", "Finance_leases.GRSS_CRRYNG_AMNT", "On_demand_and_short_notice.GRSS_CRRYNG_AMNT", "Reverse_repurchase_agreements.GRSS_CRRYNG_AMNT", "Debt_securities.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.TYP_CLLTRL", "Credit_card_debt.TYP_CLLTRL", "Trade_receivables.TYP_CLLTRL", "Advances_that_are_not_loans.TYP_CLLTRL", "Finance_leases.TYP_CLLTRL", "On_demand_and_short_notice.TYP_CLLTRL", "Reverse_repurchase_agreements.TYP_CLLTRL", "Debt_securities.TYP_CLLTRL", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152439_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Credit_card_debt.MLTLTRL_DVLPMNT_BNK_INDCTR", "Trade_receivables.MLTLTRL_DVLPMNT_BNK_INDCTR", "Advances_that_are_not_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Finance_leases.MLTLTRL_DVLPMNT_BNK_INDCTR", "On_demand_and_short_notice.MLTLTRL_DVLPMNT_BNK_INDCTR", "Reverse_repurchase_agreements.MLTLTRL_DVLPMNT_BNK_INDCTR", "Debt_securities.MLTLTRL_DVLPMNT_BNK_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152430_REF:
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Advances_that_are_not_loans.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Advances_that_are_not_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Advances_that_are_not_loans.PRTY_RL_TYP", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Advances_that_are_not_loans.TYP_INSTRMNT", "Advances_that_are_not_loans.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['120', '130', '140'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152591_REF:
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Trade_receivables.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Trade_receivables.ACCNTNG_CLSSFCTN", "Trade_receivables.HLD_SL_INDCTR", "Trade_receivables.INSTTTNL_SCTR", "Trade_receivables.PRTY_RL_TYP", "Trade_receivables.MN_DBTR_INDCTR", "Trade_receivables.TYP_INSTRMNT", "Trade_receivables.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['1020', '1023'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408950_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.TYP_CLLTRL", "Credit_card_debt.TYP_CLLTRL", "Trade_receivables.TYP_CLLTRL", "Advances_that_are_not_loans.TYP_CLLTRL", "Finance_leases.TYP_CLLTRL", "On_demand_and_short_notice.TYP_CLLTRL", "Reverse_repurchase_agreements.TYP_CLLTRL", "Debt_securities.TYP_CLLTRL", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152464_REF:
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"On_demand_and_short_notice.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.HLD_SL_INDCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "On_demand_and_short_notice.PRTY_RL_TYP", "On_demand_and_short_notice.MN_DBTR_INDCTR", "On_demand_and_short_notice.TYP_INSTRMNT", "On_demand_and_short_notice.RPYMNT_RGHTS", "On_demand_and_short_notice.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['12', '31', '522', '1201', '1202'],
					item.RPYMNT_RGHTS() in ['1'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152443_REF:
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Finance_leases.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Finance_leases.ACCNTNG_CLSSFCTN", "Finance_leases.HLD_SL_INDCTR", "Finance_leases.PRTY_RL_TYP", "Finance_leases.MN_DBTR_INDCTR", "Finance_leases.INSTTTNL_SCTR", "Finance_leases.TYP_INSTRMNT", "Finance_leases.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152453_REF:
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Advances_that_are_not_loans.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Advances_that_are_not_loans.PRTY_RL_TYP", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Advances_that_are_not_loans.TYP_INSTRMNT", "Advances_that_are_not_loans.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['120', '130', '140'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408952_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.TYP_CLLTRL", "Credit_card_debt.TYP_CLLTRL", "Trade_receivables.TYP_CLLTRL", "Advances_that_are_not_loans.TYP_CLLTRL", "Finance_leases.TYP_CLLTRL", "On_demand_and_short_notice.TYP_CLLTRL", "Reverse_repurchase_agreements.TYP_CLLTRL", "Debt_securities.TYP_CLLTRL", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152418_REF:
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={})
	def calc_referenced_items(self):
		# ERROR: No TYP_INSTRMNT found for this combination
		pass

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152426_REF:
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Trade_receivables.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Trade_receivables.ACCNTNG_CLSSFCTN", "Trade_receivables.HLD_SL_INDCTR", "Trade_receivables.MLTLTRL_DVLPMNT_BNK_INDCTR", "Trade_receivables.PRTY_RL_TYP", "Trade_receivables.MN_DBTR_INDCTR", "Trade_receivables.TYP_INSTRMNT", "Trade_receivables.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['1020', '1023'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152429_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Credit_card_debt.MLTLTRL_DVLPMNT_BNK_INDCTR", "Trade_receivables.MLTLTRL_DVLPMNT_BNK_INDCTR", "Advances_that_are_not_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Finance_leases.MLTLTRL_DVLPMNT_BNK_INDCTR", "On_demand_and_short_notice.MLTLTRL_DVLPMNT_BNK_INDCTR", "Reverse_repurchase_agreements.MLTLTRL_DVLPMNT_BNK_INDCTR", "Debt_securities.MLTLTRL_DVLPMNT_BNK_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408955_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.GRSS_CRRYNG_AMNT", "Credit_card_debt.GRSS_CRRYNG_AMNT", "Trade_receivables.GRSS_CRRYNG_AMNT", "Advances_that_are_not_loans.GRSS_CRRYNG_AMNT", "Finance_leases.GRSS_CRRYNG_AMNT", "On_demand_and_short_notice.GRSS_CRRYNG_AMNT", "Reverse_repurchase_agreements.GRSS_CRRYNG_AMNT", "Debt_securities.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.TYP_CLLTRL", "Credit_card_debt.TYP_CLLTRL", "Trade_receivables.TYP_CLLTRL", "Advances_that_are_not_loans.TYP_CLLTRL", "Finance_leases.TYP_CLLTRL", "On_demand_and_short_notice.TYP_CLLTRL", "Reverse_repurchase_agreements.TYP_CLLTRL", "Debt_securities.TYP_CLLTRL", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152440_REF:
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Advances_that_are_not_loans.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Advances_that_are_not_loans.PRTY_RL_TYP", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Advances_that_are_not_loans.TYP_INSTRMNT", "Advances_that_are_not_loans.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['120', '130', '140'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152590_REF:
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={})
	def calc_referenced_items(self):
		# ERROR: No TYP_INSTRMNT found for this combination
		pass

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408946_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Credit_card_debt.MLTLTRL_DVLPMNT_BNK_INDCTR", "Trade_receivables.MLTLTRL_DVLPMNT_BNK_INDCTR", "Advances_that_are_not_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Finance_leases.MLTLTRL_DVLPMNT_BNK_INDCTR", "On_demand_and_short_notice.MLTLTRL_DVLPMNT_BNK_INDCTR", "Reverse_repurchase_agreements.MLTLTRL_DVLPMNT_BNK_INDCTR", "Debt_securities.MLTLTRL_DVLPMNT_BNK_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.TYP_CLLTRL", "Credit_card_debt.TYP_CLLTRL", "Trade_receivables.TYP_CLLTRL", "Advances_that_are_not_loans.TYP_CLLTRL", "Finance_leases.TYP_CLLTRL", "On_demand_and_short_notice.TYP_CLLTRL", "Reverse_repurchase_agreements.TYP_CLLTRL", "Debt_securities.TYP_CLLTRL", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152445_REF:
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={})
	def calc_referenced_items(self):
		# ERROR: No TYP_INSTRMNT found for this combination
		pass

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408951_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.TYP_CLLTRL", "Credit_card_debt.TYP_CLLTRL", "Trade_receivables.TYP_CLLTRL", "Advances_that_are_not_loans.TYP_CLLTRL", "Finance_leases.TYP_CLLTRL", "On_demand_and_short_notice.TYP_CLLTRL", "Reverse_repurchase_agreements.TYP_CLLTRL", "Debt_securities.TYP_CLLTRL", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152463_REF:
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Advances_that_are_not_loans.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Advances_that_are_not_loans.PRTY_RL_TYP", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Advances_that_are_not_loans.TYP_INSTRMNT", "Advances_that_are_not_loans.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['120', '130', '140'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152452_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152424_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Non_Negotiable_bonds.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Non_Negotiable_bonds.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Non_Negotiable_bonds.HLD_SL_INDCTR", "Other_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Non_Negotiable_bonds.MLTLTRL_DVLPMNT_BNK_INDCTR", "Other_loans.PRTY_RL_TYP", "Non_Negotiable_bonds.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Non_Negotiable_bonds.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Non_Negotiable_bonds.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Non_Negotiable_bonds.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Non_Negotiable_bonds.NGTBL_SCRTY_INDCTR", "Other_loans.PRPS", "Non_Negotiable_bonds.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table
		if self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table.Non_Negotiable_bondss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152600_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.GRSS_CRRYNG_AMNT", "Credit_card_debt.GRSS_CRRYNG_AMNT", "Trade_receivables.GRSS_CRRYNG_AMNT", "Advances_that_are_not_loans.GRSS_CRRYNG_AMNT", "Finance_leases.GRSS_CRRYNG_AMNT", "On_demand_and_short_notice.GRSS_CRRYNG_AMNT", "Reverse_repurchase_agreements.GRSS_CRRYNG_AMNT", "Debt_securities.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['1'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['1'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['1'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['1'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['1'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['1'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['1'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['1'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152420_REF:
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Advances_that_are_not_loans.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Advances_that_are_not_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Advances_that_are_not_loans.PRTY_RL_TYP", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Advances_that_are_not_loans.TYP_INSTRMNT", "Advances_that_are_not_loans.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['120', '130', '140'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408947_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.TYP_CLLTRL", "Credit_card_debt.TYP_CLLTRL", "Trade_receivables.TYP_CLLTRL", "Advances_that_are_not_loans.TYP_CLLTRL", "Finance_leases.TYP_CLLTRL", "On_demand_and_short_notice.TYP_CLLTRL", "Reverse_repurchase_agreements.TYP_CLLTRL", "Debt_securities.TYP_CLLTRL", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152423_REF:
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Finance_leases.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Finance_leases.ACCNTNG_CLSSFCTN", "Finance_leases.HLD_SL_INDCTR", "Finance_leases.MLTLTRL_DVLPMNT_BNK_INDCTR", "Finance_leases.PRTY_RL_TYP", "Finance_leases.MN_DBTR_INDCTR", "Finance_leases.TYP_INSTRMNT", "Finance_leases.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408949_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.TYP_CLLTRL", "Credit_card_debt.TYP_CLLTRL", "Trade_receivables.TYP_CLLTRL", "Advances_that_are_not_loans.TYP_CLLTRL", "Finance_leases.TYP_CLLTRL", "On_demand_and_short_notice.TYP_CLLTRL", "Reverse_repurchase_agreements.TYP_CLLTRL", "Debt_securities.TYP_CLLTRL", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152465_REF:
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Credit_card_debt.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Credit_card_debt.ACCNTNG_CLSSFCTN", "Credit_card_debt.HLD_SL_INDCTR", "Credit_card_debt.INSTTTNL_SCTR", "Credit_card_debt.PRTY_RL_TYP", "Credit_card_debt.MN_DBTR_INDCTR", "Credit_card_debt.TYP_INSTRMNT", "Credit_card_debt.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['51'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152417_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Non_Negotiable_bonds.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Non_Negotiable_bonds.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Non_Negotiable_bonds.HLD_SL_INDCTR", "Other_loans.INSTTTNL_SCTR", "Non_Negotiable_bonds.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Non_Negotiable_bonds.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Non_Negotiable_bonds.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Non_Negotiable_bonds.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Non_Negotiable_bonds.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Non_Negotiable_bonds.NGTBL_SCRTY_INDCTR", "Other_loans.PRPS", "Non_Negotiable_bonds.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table
		if self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table.Non_Negotiable_bondss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152457_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Non_Negotiable_bonds.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Non_Negotiable_bonds.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Non_Negotiable_bonds.HLD_SL_INDCTR", "Other_loans.INSTTTNL_SCTR", "Non_Negotiable_bonds.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Non_Negotiable_bonds.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Non_Negotiable_bonds.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Non_Negotiable_bonds.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Non_Negotiable_bonds.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Non_Negotiable_bonds.NGTBL_SCRTY_INDCTR", "Other_loans.PRPS", "Non_Negotiable_bonds.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table
		if self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table.Non_Negotiable_bondss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152454_REF:
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"On_demand_and_short_notice.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.HLD_SL_INDCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "On_demand_and_short_notice.PRTY_RL_TYP", "On_demand_and_short_notice.MN_DBTR_INDCTR", "On_demand_and_short_notice.TYP_INSTRMNT", "On_demand_and_short_notice.RPYMNT_RGHTS", "On_demand_and_short_notice.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['12', '31', '522', '1201', '1202'],
					item.RPYMNT_RGHTS() in ['1'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152416_REF:
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Finance_leases.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Finance_leases.ACCNTNG_CLSSFCTN", "Finance_leases.HLD_SL_INDCTR", "Finance_leases.INSTTTNL_SCTR", "Finance_leases.PRTY_RL_TYP", "Finance_leases.MN_DBTR_INDCTR", "Finance_leases.TYP_INSTRMNT", "Finance_leases.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408948_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.TYP_CLLTRL", "Credit_card_debt.TYP_CLLTRL", "Trade_receivables.TYP_CLLTRL", "Advances_that_are_not_loans.TYP_CLLTRL", "Finance_leases.TYP_CLLTRL", "On_demand_and_short_notice.TYP_CLLTRL", "Reverse_repurchase_agreements.TYP_CLLTRL", "Debt_securities.TYP_CLLTRL", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152598_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.GRSS_CRRYNG_AMNT", "Credit_card_debt.GRSS_CRRYNG_AMNT", "Trade_receivables.GRSS_CRRYNG_AMNT", "Advances_that_are_not_loans.GRSS_CRRYNG_AMNT", "Finance_leases.GRSS_CRRYNG_AMNT", "On_demand_and_short_notice.GRSS_CRRYNG_AMNT", "Reverse_repurchase_agreements.GRSS_CRRYNG_AMNT", "Debt_securities.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152446_REF:
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Trade_receivables.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Trade_receivables.ACCNTNG_CLSSFCTN", "Trade_receivables.HLD_SL_INDCTR", "Trade_receivables.PRTY_RL_TYP", "Trade_receivables.MN_DBTR_INDCTR", "Trade_receivables.INSTTTNL_SCTR", "Trade_receivables.TYP_INSTRMNT", "Trade_receivables.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['1020', '1023'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152456_REF:
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Finance_leases.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Finance_leases.ACCNTNG_CLSSFCTN", "Finance_leases.HLD_SL_INDCTR", "Finance_leases.INSTTTNL_SCTR", "Finance_leases.PRTY_RL_TYP", "Finance_leases.MN_DBTR_INDCTR", "Finance_leases.TYP_INSTRMNT", "Finance_leases.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152588_REF:
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Finance_leases.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Finance_leases.ACCNTNG_CLSSFCTN", "Finance_leases.HLD_SL_INDCTR", "Finance_leases.INSTTTNL_SCTR", "Finance_leases.PRTY_RL_TYP", "Finance_leases.MN_DBTR_INDCTR", "Finance_leases.TYP_INSTRMNT", "Finance_leases.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152455_REF:
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Credit_card_debt.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Credit_card_debt.ACCNTNG_CLSSFCTN", "Credit_card_debt.HLD_SL_INDCTR", "Credit_card_debt.INSTTTNL_SCTR", "Credit_card_debt.PRTY_RL_TYP", "Credit_card_debt.MN_DBTR_INDCTR", "Credit_card_debt.TYP_INSTRMNT", "Credit_card_debt.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['51'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408942_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.TYP_CLLTRL", "Credit_card_debt.TYP_CLLTRL", "Trade_receivables.TYP_CLLTRL", "Advances_that_are_not_loans.TYP_CLLTRL", "Finance_leases.TYP_CLLTRL", "On_demand_and_short_notice.TYP_CLLTRL", "Reverse_repurchase_agreements.TYP_CLLTRL", "Debt_securities.TYP_CLLTRL", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152441_REF:
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"On_demand_and_short_notice.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.HLD_SL_INDCTR", "On_demand_and_short_notice.PRTY_RL_TYP", "On_demand_and_short_notice.MN_DBTR_INDCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "On_demand_and_short_notice.TYP_INSTRMNT", "On_demand_and_short_notice.RPYMNT_RGHTS", "On_demand_and_short_notice.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['12', '31', '522', '1201', '1202'],
					item.RPYMNT_RGHTS() in ['1'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152449_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152466_REF:
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Finance_leases.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Finance_leases.ACCNTNG_CLSSFCTN", "Finance_leases.HLD_SL_INDCTR", "Finance_leases.INSTTTNL_SCTR", "Finance_leases.PRTY_RL_TYP", "Finance_leases.MN_DBTR_INDCTR", "Finance_leases.TYP_INSTRMNT", "Finance_leases.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408945_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Credit_card_debt.MLTLTRL_DVLPMNT_BNK_INDCTR", "Trade_receivables.MLTLTRL_DVLPMNT_BNK_INDCTR", "Advances_that_are_not_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Finance_leases.MLTLTRL_DVLPMNT_BNK_INDCTR", "On_demand_and_short_notice.MLTLTRL_DVLPMNT_BNK_INDCTR", "Reverse_repurchase_agreements.MLTLTRL_DVLPMNT_BNK_INDCTR", "Debt_securities.MLTLTRL_DVLPMNT_BNK_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.TYP_CLLTRL", "Credit_card_debt.TYP_CLLTRL", "Trade_receivables.TYP_CLLTRL", "Advances_that_are_not_loans.TYP_CLLTRL", "Finance_leases.TYP_CLLTRL", "On_demand_and_short_notice.TYP_CLLTRL", "Reverse_repurchase_agreements.TYP_CLLTRL", "Debt_securities.TYP_CLLTRL", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152589_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Non_Negotiable_bonds.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Non_Negotiable_bonds.HLD_SL_INDCTR", "Other_loans.INSTTTNL_SCTR", "Non_Negotiable_bonds.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Non_Negotiable_bonds.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Non_Negotiable_bonds.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Non_Negotiable_bonds.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Non_Negotiable_bonds.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Non_Negotiable_bonds.NGTBL_SCRTY_INDCTR", "Other_loans.PRPS", "Non_Negotiable_bonds.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152434_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Non_Negotiable_bonds.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Non_Negotiable_bonds.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Non_Negotiable_bonds.HLD_SL_INDCTR", "Other_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Non_Negotiable_bonds.MLTLTRL_DVLPMNT_BNK_INDCTR", "Other_loans.PRTY_RL_TYP", "Non_Negotiable_bonds.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Non_Negotiable_bonds.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Non_Negotiable_bonds.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Non_Negotiable_bonds.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Non_Negotiable_bonds.NGTBL_SCRTY_INDCTR", "Other_loans.PRPS", "Non_Negotiable_bonds.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table
		if self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table.Non_Negotiable_bondss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152432_REF:
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Credit_card_debt.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Credit_card_debt.ACCNTNG_CLSSFCTN", "Credit_card_debt.HLD_SL_INDCTR", "Credit_card_debt.MLTLTRL_DVLPMNT_BNK_INDCTR", "Credit_card_debt.PRTY_RL_TYP", "Credit_card_debt.MN_DBTR_INDCTR", "Credit_card_debt.TYP_INSTRMNT", "Credit_card_debt.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['51'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152415_REF:
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Credit_card_debt.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Credit_card_debt.ACCNTNG_CLSSFCTN", "Credit_card_debt.HLD_SL_INDCTR", "Credit_card_debt.INSTTTNL_SCTR", "Credit_card_debt.PRTY_RL_TYP", "Credit_card_debt.MN_DBTR_INDCTR", "Credit_card_debt.TYP_INSTRMNT", "Credit_card_debt.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['51'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152585_REF:
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Advances_that_are_not_loans.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Advances_that_are_not_loans.PRTY_RL_TYP", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Advances_that_are_not_loans.TYP_INSTRMNT", "Advances_that_are_not_loans.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['120', '130', '140'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152444_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Non_Negotiable_bonds.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Non_Negotiable_bonds.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Non_Negotiable_bonds.HLD_SL_INDCTR", "Other_loans.PRTY_RL_TYP", "Non_Negotiable_bonds.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Non_Negotiable_bonds.MN_DBTR_INDCTR", "Other_loans.INSTTTNL_SCTR", "Non_Negotiable_bonds.INSTTTNL_SCTR", "Other_loans.TYP_INSTRMNT", "Non_Negotiable_bonds.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Non_Negotiable_bonds.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Non_Negotiable_bonds.NGTBL_SCRTY_INDCTR", "Other_loans.PRPS", "Non_Negotiable_bonds.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table
		if self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table.Non_Negotiable_bondss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152601_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.GRSS_CRRYNG_AMNT", "Credit_card_debt.GRSS_CRRYNG_AMNT", "Trade_receivables.GRSS_CRRYNG_AMNT", "Advances_that_are_not_loans.GRSS_CRRYNG_AMNT", "Finance_leases.GRSS_CRRYNG_AMNT", "On_demand_and_short_notice.GRSS_CRRYNG_AMNT", "Reverse_repurchase_agreements.GRSS_CRRYNG_AMNT", "Debt_securities.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['12'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['12'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['12'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['12'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['12'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['12'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['12'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['12'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152414_REF:
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"On_demand_and_short_notice.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.HLD_SL_INDCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "On_demand_and_short_notice.PRTY_RL_TYP", "On_demand_and_short_notice.MN_DBTR_INDCTR", "On_demand_and_short_notice.TYP_INSTRMNT", "On_demand_and_short_notice.RPYMNT_RGHTS", "On_demand_and_short_notice.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['12', '31', '522', '1201', '1202'],
					item.RPYMNT_RGHTS() in ['1'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152421_REF:
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"On_demand_and_short_notice.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.HLD_SL_INDCTR", "On_demand_and_short_notice.MLTLTRL_DVLPMNT_BNK_INDCTR", "On_demand_and_short_notice.PRTY_RL_TYP", "On_demand_and_short_notice.MN_DBTR_INDCTR", "On_demand_and_short_notice.TYP_INSTRMNT", "On_demand_and_short_notice.RPYMNT_RGHTS", "On_demand_and_short_notice.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['12', '31', '522', '1201', '1202'],
					item.RPYMNT_RGHTS() in ['1'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_441809_REF:
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Trade_receivables.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Trade_receivables.ACCNTNG_CLSSFCTN", "Trade_receivables.HLD_SL_INDCTR", "Trade_receivables.INSTTTNL_SCTR", "Trade_receivables.PRTY_RL_TYP", "Trade_receivables.MN_DBTR_INDCTR", "Trade_receivables.TYP_INSTRMNT", "Trade_receivables.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['1020', '1023'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152472_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152458_REF:
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={})
	def calc_referenced_items(self):
		# ERROR: No TYP_INSTRMNT found for this combination
		pass

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152431_REF:
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"On_demand_and_short_notice.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.HLD_SL_INDCTR", "On_demand_and_short_notice.MLTLTRL_DVLPMNT_BNK_INDCTR", "On_demand_and_short_notice.PRTY_RL_TYP", "On_demand_and_short_notice.MN_DBTR_INDCTR", "On_demand_and_short_notice.TYP_INSTRMNT", "On_demand_and_short_notice.RPYMNT_RGHTS", "On_demand_and_short_notice.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['12', '31', '522', '1201', '1202'],
					item.RPYMNT_RGHTS() in ['1'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152435_REF:
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={})
	def calc_referenced_items(self):
		# ERROR: No TYP_INSTRMNT found for this combination
		pass

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152442_REF:
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Credit_card_debt.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Credit_card_debt.ACCNTNG_CLSSFCTN", "Credit_card_debt.HLD_SL_INDCTR", "Credit_card_debt.PRTY_RL_TYP", "Credit_card_debt.MN_DBTR_INDCTR", "Credit_card_debt.INSTTTNL_SCTR", "Credit_card_debt.TYP_INSTRMNT", "Credit_card_debt.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['51'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152469_REF:
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Trade_receivables.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Trade_receivables.ACCNTNG_CLSSFCTN", "Trade_receivables.HLD_SL_INDCTR", "Trade_receivables.INSTTTNL_SCTR", "Trade_receivables.PRTY_RL_TYP", "Trade_receivables.MN_DBTR_INDCTR", "Trade_receivables.TYP_INSTRMNT", "Trade_receivables.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['1020', '1023'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152451_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['12'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['12'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['12'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['12'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['12'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['12'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['12'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['12'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152468_REF:
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={})
	def calc_referenced_items(self):
		# ERROR: No TYP_INSTRMNT found for this combination
		pass

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152419_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152413_REF:
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Advances_that_are_not_loans.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Advances_that_are_not_loans.PRTY_RL_TYP", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Advances_that_are_not_loans.TYP_INSTRMNT", "Advances_that_are_not_loans.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['120', '130', '140'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152459_REF:
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Trade_receivables.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Trade_receivables.ACCNTNG_CLSSFCTN", "Trade_receivables.HLD_SL_INDCTR", "Trade_receivables.INSTTTNL_SCTR", "Trade_receivables.PRTY_RL_TYP", "Trade_receivables.MN_DBTR_INDCTR", "Trade_receivables.TYP_INSTRMNT", "Trade_receivables.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['1020', '1023'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152425_REF:
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={})
	def calc_referenced_items(self):
		# ERROR: No TYP_INSTRMNT found for this combination
		pass

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152586_REF:
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"On_demand_and_short_notice.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.HLD_SL_INDCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "On_demand_and_short_notice.PRTY_RL_TYP", "On_demand_and_short_notice.MN_DBTR_INDCTR", "On_demand_and_short_notice.TYP_INSTRMNT", "On_demand_and_short_notice.RPYMNT_RGHTS", "On_demand_and_short_notice.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['12', '31', '522', '1201', '1202'],
					item.RPYMNT_RGHTS() in ['1'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152584_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.GRSS_CRRYNG_AMNT", "Credit_card_debt.GRSS_CRRYNG_AMNT", "Trade_receivables.GRSS_CRRYNG_AMNT", "Advances_that_are_not_loans.GRSS_CRRYNG_AMNT", "Finance_leases.GRSS_CRRYNG_AMNT", "On_demand_and_short_notice.GRSS_CRRYNG_AMNT", "Reverse_repurchase_agreements.GRSS_CRRYNG_AMNT", "Debt_securities.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152587_REF:
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Credit_card_debt.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Credit_card_debt.ACCNTNG_CLSSFCTN", "Credit_card_debt.HLD_SL_INDCTR", "Credit_card_debt.INSTTTNL_SCTR", "Credit_card_debt.PRTY_RL_TYP", "Credit_card_debt.MN_DBTR_INDCTR", "Credit_card_debt.TYP_INSTRMNT", "Credit_card_debt.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S11', 'S15', 'S124', 'S126', 'S127', 'S123', 'S128', 'S129', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S1312', 'S1313', 'S1311', 'S1314', 'S14_B', 'S14_A'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['51'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152422_REF:
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Credit_card_debt.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Credit_card_debt.ACCNTNG_CLSSFCTN", "Credit_card_debt.HLD_SL_INDCTR", "Credit_card_debt.MLTLTRL_DVLPMNT_BNK_INDCTR", "Credit_card_debt.PRTY_RL_TYP", "Credit_card_debt.MN_DBTR_INDCTR", "Credit_card_debt.TYP_INSTRMNT", "Credit_card_debt.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['51'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152436_REF:
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Trade_receivables.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Trade_receivables.ACCNTNG_CLSSFCTN", "Trade_receivables.HLD_SL_INDCTR", "Trade_receivables.MLTLTRL_DVLPMNT_BNK_INDCTR", "Trade_receivables.PRTY_RL_TYP", "Trade_receivables.MN_DBTR_INDCTR", "Trade_receivables.TYP_INSTRMNT", "Trade_receivables.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['1020', '1023'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152462_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152450_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['1'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['1'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['1'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['1'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['1'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['1'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['1'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['1'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152467_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Non_Negotiable_bonds.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Non_Negotiable_bonds.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Non_Negotiable_bonds.HLD_SL_INDCTR", "Other_loans.INSTTTNL_SCTR", "Non_Negotiable_bonds.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Non_Negotiable_bonds.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Non_Negotiable_bonds.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Non_Negotiable_bonds.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Non_Negotiable_bonds.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Non_Negotiable_bonds.NGTBL_SCRTY_INDCTR", "Other_loans.PRPS", "Non_Negotiable_bonds.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table
		if self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table.Non_Negotiable_bondss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408943_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Credit_card_debt.MLTLTRL_DVLPMNT_BNK_INDCTR", "Trade_receivables.MLTLTRL_DVLPMNT_BNK_INDCTR", "Advances_that_are_not_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Finance_leases.MLTLTRL_DVLPMNT_BNK_INDCTR", "On_demand_and_short_notice.MLTLTRL_DVLPMNT_BNK_INDCTR", "Reverse_repurchase_agreements.MLTLTRL_DVLPMNT_BNK_INDCTR", "Debt_securities.MLTLTRL_DVLPMNT_BNK_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.TYP_CLLTRL", "Credit_card_debt.TYP_CLLTRL", "Trade_receivables.TYP_CLLTRL", "Advances_that_are_not_loans.TYP_CLLTRL", "Finance_leases.TYP_CLLTRL", "On_demand_and_short_notice.TYP_CLLTRL", "Reverse_repurchase_agreements.TYP_CLLTRL", "Debt_securities.TYP_CLLTRL", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408944_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Credit_card_debt.MLTLTRL_DVLPMNT_BNK_INDCTR", "Trade_receivables.MLTLTRL_DVLPMNT_BNK_INDCTR", "Advances_that_are_not_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Finance_leases.MLTLTRL_DVLPMNT_BNK_INDCTR", "On_demand_and_short_notice.MLTLTRL_DVLPMNT_BNK_INDCTR", "Reverse_repurchase_agreements.MLTLTRL_DVLPMNT_BNK_INDCTR", "Debt_securities.MLTLTRL_DVLPMNT_BNK_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.TYP_INSTRMNT", "Credit_card_debt.TYP_INSTRMNT", "Trade_receivables.TYP_INSTRMNT", "Advances_that_are_not_loans.TYP_INSTRMNT", "Finance_leases.TYP_INSTRMNT", "On_demand_and_short_notice.TYP_INSTRMNT", "Reverse_repurchase_agreements.TYP_INSTRMNT", "Debt_securities.TYP_INSTRMNT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR", "Other_loans.TYP_CLLTRL", "Credit_card_debt.TYP_CLLTRL", "Trade_receivables.TYP_CLLTRL", "Advances_that_are_not_loans.TYP_CLLTRL", "Finance_leases.TYP_CLLTRL", "On_demand_and_short_notice.TYP_CLLTRL", "Reverse_repurchase_agreements.TYP_CLLTRL", "Debt_securities.TYP_CLLTRL", "Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80', '51', '1022'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
					item.TYP_CLLTRL() in ['17', '2', '77', '78', '12', '3', '89', '13', '85', '86', '84', '10', '81', '83', '66', '111', '110', '106', '108', '107'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152433_REF:
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Finance_leases.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Finance_leases.ACCNTNG_CLSSFCTN", "Finance_leases.HLD_SL_INDCTR", "Finance_leases.MLTLTRL_DVLPMNT_BNK_INDCTR", "Finance_leases.PRTY_RL_TYP", "Finance_leases.MN_DBTR_INDCTR", "Finance_leases.TYP_INSTRMNT", "Finance_leases.PRPS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.TYP_INSTRMNT() in ['80'],
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None
