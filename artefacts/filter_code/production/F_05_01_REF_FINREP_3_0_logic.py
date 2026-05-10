from pybirdai.models.bird_data_model import *
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.process_steps.pybird.csv_converter import CSVConverter
from datetime import datetime
from pybirdai.annotations.decorators import lineage, track_table_init



class F_05_01_REF_FINREP_3_0_Base:
	def GRSS_CRRYNG_AMNT() -> int:
		pass
	def ACCNTNG_CLSSFCTN() -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		pass
	def HLD_SL_INDCTR() -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		pass
	def SBJCT_IMPRMNT_INDCTR() -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		pass
	def INSTTTNL_SCTR() -> str:
		''' return string from INSTTTNL_SCTR enumeration '''
		pass
	def MLTLTRL_DVLPMNT_BNK_INDCTR() -> str:
		''' return string from MLTLTRL_DVLPMNT_BNK_INDCTR enumeration '''
		pass
	def PRTY_RL_TYP() -> str:
		''' return string from ENTTY_RL_TYP enumeration '''
		pass
	def MN_DBTR_INDCTR() -> str:
		''' return string from MN_DBTR_INDCTR enumeration '''
		pass
	def TYP_INSTRMNT() -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		pass
	def RPYMNT_RGHTS() -> str:
		''' return string from RPYMNT_RGHTS enumeration '''
		pass
	def NGTBL_SCRTY_INDCTR() -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		pass
	def TYP_CLLTRL() -> str:
		''' return string from TYP_PRTCTN enumeration '''
		pass
	def PRPS() -> str:
		''' return string from PRPS enumeration '''
		pass
	def CRRYNG_AMNT() -> int:
		pass
	def SPCLSD_LNDNG_EXPSR_TYP() -> str:
		''' return string from SPCLSD_LNDNG_EXPSR_TYP enumeration '''
		pass

	

class Advances_that_are_not_loans(F_05_01_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	def NGTBL_SCRTY_INDCTR(self):
		''' return string from NGTBL_SCRTY enumeration of 2 for non-negotiable '''
		return '2'
	def RPYMNT_RGHTS(self):
		''' return string from RPYMNT_RGHTS enumeration of 2 fro Other_than_on_demand_or_short_notice'''
		return '2'	
	def MN_DBTR_INDCTR(self):
		# return 1 for main debtor
		return '1'
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.GRSS_CRRYNG_AMNT
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.PRPS"})
	def PRPS(self):
		return self.INSTRMNT_RL.PRPS
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
	INSTRMNT_ENTTY_RL_ASSGNMNT = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.ENTTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.ENTTY_RL_TYP
	CLLTRL = None # CLLTRL
	@lineage(dependencies={"CLLTRL.CLLTRL_TYP"})
	def TYP_CLLTRL(self):
		if self.CLLTRL is not None:
			return self.CLLTRL.TYP_CLLTRL
		return '0'
	@lineage(dependencies={"INSTRMNT_RL.SPCLSD_LNDNG_EXPSR_TYP"})
	def SPCLSD_LNDNG_EXPSR_TYP(self):
		return self.INSTRMNT_RL.SPCLSD_LNDNG_EXPSR_TYP

class Other_loans(F_05_01_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	def RPYMNT_RGHTS(self):
		''' return string from RPYMNT_RGHTS enumeration of 2 fro Other_than_on_demand_or_short_notice'''
		return '2'	
	def NGTBL_SCRTY_INDCTR(self):
		''' return string from NGTBL_SCRTY enumeration of 2 for non-negotiable '''
		return '2'
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.GRSS_CRRYNG_AMNT
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.PRPS"})
	def PRPS(self):
		return self.INSTRMNT_RL.PRPS
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
	INSTRMNT_ENTTY_RL_ASSGNMNT = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.ENTTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.ENTTY_RL_TYP
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.MN_DBTR_INDCTR"})
	def MN_DBTR_INDCTR(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.MN_DBTR_INDCTR
	CLLTRL = None # CLLTRL
	@lineage(dependencies={"CLLTRL.CLLTRL_TYP"})
	def TYP_CLLTRL(self):
		if self.CLLTRL is not None:
			return self.CLLTRL.TYP_CLLTRL
		return '0'
	@lineage(dependencies={"INSTRMNT_RL.SPCLSD_LNDNG_EXPSR_TYP"})
	def SPCLSD_LNDNG_EXPSR_TYP(self):
		return self.INSTRMNT_RL.SPCLSD_LNDNG_EXPSR_TYP
	ENTTY_RL = None # ENTTY_RL

class Credit_card_debt(F_05_01_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	def NGTBL_SCRTY_INDCTR(self):
		''' return string from NGTBL_SCRTY enumeration of 2 for non-negotiable '''
		return '2'
	def RPYMNT_RGHTS(self):
		''' return string from RPYMNT_RGHTS enumeration of 2 fro Other_than_on_demand_or_short_notice'''
		return '2'	
	def MN_DBTR_INDCTR(self):
		# return 1 for main debtor
		return '1'
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.GRSS_CRRYNG_AMNT
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.PRPS"})
	def PRPS(self):
		return self.INSTRMNT_RL.PRPS
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
	INSTRMNT_ENTTY_RL_ASSGNMNT = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.ENTTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.ENTTY_RL_TYP
	CLLTRL = None # CLLTRL
	@lineage(dependencies={"CLLTRL.CLLTRL_TYP"})
	def TYP_CLLTRL(self):
		if self.CLLTRL is not None:
			return self.CLLTRL.TYP_CLLTRL
		return '0'
	@lineage(dependencies={"INSTRMNT_RL.SPCLSD_LNDNG_EXPSR_TYP"})
	def SPCLSD_LNDNG_EXPSR_TYP(self):
		return self.INSTRMNT_RL.SPCLSD_LNDNG_EXPSR_TYP

class Trade_receivables(F_05_01_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	def NGTBL_SCRTY_INDCTR(self):
		''' return string from NGTBL_SCRTY enumeration of 2 for non-negotiable '''
		return '2'
	def RPYMNT_RGHTS(self):
		''' return string from RPYMNT_RGHTS enumeration of 2 fro Other_than_on_demand_or_short_notice'''
		return '2'	
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.GRSS_CRRYNG_AMNT
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.PRPS"})
	def PRPS(self):
		return self.INSTRMNT_RL.PRPS
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
	INSTRMNT_ENTTY_RL_ASSGNMNT = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.ENTTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.ENTTY_RL_TYP
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.MN_DBTR_INDCTR"})
	def MN_DBTR_INDCTR(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.MN_DBTR_INDCTR
	CLLTRL = None # CLLTRL
	@lineage(dependencies={"CLLTRL.CLLTRL_TYP"})
	def TYP_CLLTRL(self):
		if self.CLLTRL is not None:
			return self.CLLTRL.TYP_CLLTRL
		return '0'
	@lineage(dependencies={"INSTRMNT_RL.SPCLSD_LNDNG_EXPSR_TYP"})
	def SPCLSD_LNDNG_EXPSR_TYP(self):
		return self.INSTRMNT_RL.SPCLSD_LNDNG_EXPSR_TYP

class Finance_leases(F_05_01_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	@lineage(dependencies={"INSTRMNT.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self):
		return self.INSTRMNT.RPYMNT_RGHTS
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.GRSS_CRRYNG_AMNT
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.PRPS"})
	def PRPS(self):
		return self.INSTRMNT_RL.PRPS
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
	INSTRMNT_ENTTY_RL_ASSGNMNT = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.ENTTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.ENTTY_RL_TYP
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.MN_DBTR_INDCTR"})
	def MN_DBTR_INDCTR(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.MN_DBTR_INDCTR
	CLLTRL = None # CLLTRL
	@lineage(dependencies={"CLLTRL.CLLTRL_TYP"})
	def TYP_CLLTRL(self):
		if self.CLLTRL is not None:
			return self.CLLTRL.TYP_CLLTRL
		return '0'
	def NGTBL_SCRTY_INDCTR(self):
		''' return string from NGTBL_SCRTY enumeration of 2 for non-negotiable '''
		return '2'
	@lineage(dependencies={"INSTRMNT_RL.SPCLSD_LNDNG_EXPSR_TYP"})
	def SPCLSD_LNDNG_EXPSR_TYP(self):
		return self.INSTRMNT_RL.SPCLSD_LNDNG_EXPSR_TYP

class On_demand_and_short_notice(F_05_01_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	@lineage(dependencies={"INSTRMNT.RPYMNT_RGHTS"})
	def RPYMNT_RGHTS(self):
		return self.INSTRMNT.RPYMNT_RGHTS
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.GRSS_CRRYNG_AMNT
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.PRPS"})
	def PRPS(self):
		return self.INSTRMNT_RL.PRPS
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
	INSTRMNT_ENTTY_RL_ASSGNMNT = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.ENTTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.ENTTY_RL_TYP
	def MN_DBTR_INDCTR(self):
		# return 1 for main debtor
		return '1'
	def NGTBL_SCRTY_INDCTR(self):
		''' return string from NGTBL_SCRTY enumeration of 2 for non-negotiable '''
		return '2'
	def TYP_CLLTRL(self):
		return '0'
	@lineage(dependencies={"INSTRMNT_RL.SPCLSD_LNDNG_EXPSR_TYP"})
	def SPCLSD_LNDNG_EXPSR_TYP(self):
		return self.INSTRMNT_RL.SPCLSD_LNDNG_EXPSR_TYP

class Reverse_repurchase_agreements(F_05_01_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.INSTRMNT_TYP_PRDCT
	def RPYMNT_RGHTS(self):
		''' return string from RPYMNT_RGHTS enumeration of 2 fro Other_than_on_demand_or_short_notice'''
		return '2'
	def NGTBL_SCRTY_INDCTR(self):
		''' return string from NGTBL_SCRTY enumeration of 2 for non-negotiable '''
		return '2'
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.GRSS_CRRYNG_AMNT
	@lineage(dependencies={"INSTRMNT_RL.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.INSTRMNT_RL.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"INSTRMNT_RL.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.INSTRMNT_RL.HLD_SL_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	@lineage(dependencies={"INSTRMNT_RL.PRPS"})
	def PRPS(self):
		return self.INSTRMNT_RL.PRPS
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
	INSTRMNT_ENTTY_RL_ASSGNMNT = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	@lineage(dependencies={"INSTRMNT_ENTTY_RL_ASSGNMNT.ENTTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.INSTRMNT_ENTTY_RL_ASSGNMNT.ENTTY_RL_TYP
	def MN_DBTR_INDCTR(self):
		# return 1 for main debtor
		return '1'
	def TYP_CLLTRL(self):
		return '0'
	@lineage(dependencies={"INSTRMNT_RL.SPCLSD_LNDNG_EXPSR_TYP"})
	def SPCLSD_LNDNG_EXPSR_TYP(self):
		return self.INSTRMNT_RL.SPCLSD_LNDNG_EXPSR_TYP

class Debt_securities(F_05_01_REF_FINREP_3_0_Base):
	LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT = None # LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT
	@lineage(dependencies={"LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self):
		return self.LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT.GRSS_CRRYNG_AMNT
	@lineage(dependencies={"LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT.SBJCT_IMPRMNT_INDCTR
	@lineage(dependencies={"LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT.CRRYNG_AMNT
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
	SCRTY_EXCHNG_TRDBL_DRVTV = None # SCRTY_EXCHNG_TRDBL_DRVTV
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR
	EXCHNG_TRDBL_DRVTV_PSTN = None # EXCHNG_TRDBL_DRVTV_PSTN
	@lineage(dependencies={"EXCHNG_TRDBL_DRVTV_PSTN.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.EXCHNG_TRDBL_DRVTV_PSTN.HLD_SL_INDCTR
	SCRTY_ENTTY_RL_ASSGNMNT = None # SCRTY_ENTTY_RL_ASSGNMNT
	@lineage(dependencies={"SCRTY_ENTTY_RL_ASSGNMNT.ENTTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.SCRTY_ENTTY_RL_ASSGNMNT.ENTTY_RL_TYP
	def TYP_CLLTRL(self):
		return '0'
	@lineage(dependencies={"INSTRMNT_RL.SPCLSD_LNDNG_EXPSR_TYP"})
	def SPCLSD_LNDNG_EXPSR_TYP(self):
		return self.INSTRMNT_RL.SPCLSD_LNDNG_EXPSR_TYP

class Non_Negotiable_bonds(F_05_01_REF_FINREP_3_0_Base):
	LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT = None # LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT
	LNG_SHRT_BLNC_SHT_RCGNSD_SCRTY_PSTN = None # LNG_SHRT_BLNC_SHT_RCGNSD_SCRTY_PSTN
	BLNC_SHT_RCGNSD_NN_BLNC_SHT_RCGNSD_SCRTY_PSTN = None # BLNC_SHT_RCGNSD_NN_BLNC_SHT_RCGNSD_SCRTY_PSTN
	SCRTY_PSTN = None # SCRTY_PSTN
	SCRTY_EXCHNG_TRDBL_DRVTV = None # SCRTY_EXCHNG_TRDBL_DRVTV
	@lineage(dependencies={"LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT.GRSS_CRRYNG_AMNT"})
	def GRSS_CRRYNG_AMNT(self):
		return self.LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT.GRSS_CRRYNG_AMNT
	@lineage(dependencies={"LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self):
		return self.LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT.ACCNTNG_CLSSFCTN
	@lineage(dependencies={"LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT.SBJCT_IMPRMNT_INDCTR
	@lineage(dependencies={"LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT.CRRYNG_AMNT
	PRTY = None # PRTY
	@lineage(dependencies={"PRTY.INSTTTNL_SCTR"})
	def INSTTTNL_SCTR(self):
		return self.PRTY.INSTTTNL_SCTR
	@lineage(dependencies={"PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR"})
	def MLTLTRL_DVLPMNT_BNK_INDCTR(self):
		return self.PRTY.MLTLTRL_DVLPMNT_BNK_INDCTR
	SCRTY_EXCHNG_TRDBL_DRVTV = None # SCRTY_EXCHNG_TRDBL_DRVTV
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR
	@lineage(dependencies={"LNG_SHRT_BLNC_SHT_RCGNSD_SCRTY_PSTN.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self):
		return self.LNG_SHRT_BLNC_SHT_RCGNSD_SCRTY_PSTN.HLD_SL_INDCTR
	SCRTY_ENTTY_RL_ASSGNMNT = None # SCRTY_ENTTY_RL_ASSGNMNT
	@lineage(dependencies={"SCRTY_ENTTY_RL_ASSGNMNT.ENTTY_RL_TYP"})
	def PRTY_RL_TYP(self):
		return self.SCRTY_ENTTY_RL_ASSGNMNT.ENTTY_RL_TYP
	def TYP_CLLTRL(self):
		return '0'
	def PRPS(self):
		return '19'
	def RPYMNT_RGHTS(self):
		''' return string from RPYMNT_RGHTS enumeration '''
		return '2'
	def TYP_INSTRMNT(self):
		''' return string from INSTRMNT_TYP_PRDCT enumeration '''
		return '1022'
	def SPCLSD_LNDNG_EXPSR_TYP(self):
		return '0'
	def MN_DBTR_INDCTR(self):
		# return 1 for main debtor
		return '1'
    
class F_05_01_REF_FINREP_3_0_Other_loans_Table:
	CLLTRL_Table = None # CLLTRL
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_ENTTY_RL_ASSGNMNT_Table = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	PRTY_Table = None # PRTY
	ENTTY_RL_Table = None # ENTTY_RL
	Other_loanss = []# Other_loans[]	
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theINSTRMNT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theENTTY_RL",		
		"ENTTY_RL.thePRTY",
		"INSTRMNT.INSTRMNT_uniqueID",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.INSTRMNT_ENTTY_RL_ASSGNMNT_uniqueID",
		"PRTY.PRTY_uniqueID",
		"INSTRMNT_RL.theINSTRMNT"
		})
	def calc_Other_loanss(self) :
		
		items = [] # Other_loans[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		
		for instrmnt_rl in self.INSTRMNT_RL_Table:
			typeInst = instrmnt_rl.theINSTRMNT.INSTRMNT_TYP_PRDCT
			#if (typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['140']) or \
			#		(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['1022'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['51'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['80'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['12'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['522'] ):
			if (typeInst == '1022' ):
				
				newItem = Other_loans()
				newItem.INSTRMNT_RL = instrmnt_rl
				newItem.INSTRMNT = instrmnt_rl.theINSTRMNT
				
				for era in  self.INSTRMNT_ENTTY_RL_ASSGNMNT_Table:
					inst = era.theINSTRMNT
					if (inst == newItem.INSTRMNT):
						newItem.INSTRMNT_ENTTY_RL_ASSGNMNT = era
						er = era.theENTTY_RL
						newItem.ENTTY_RL = er
						newItem.PRTY = er.thePRTY
					
				items.append(newItem)
	
		return items
	@track_table_init
	def init(self):
		Orchestration().init(self)
		self.Other_loanss = []
		self.Other_loanss.extend(self.calc_Other_loanss())
		
		# Explicitly track the created Other_loans objects for lineage
		#from pybirdai.annotations.decorators import _lineage_context
		#orchestration = _lineage_context.get('orchestration')
		#if orchestration and hasattr(orchestration, 'track_data_processing'):
		#	print(f"🔍 Other_loans_Table: Tracking {len(self.Other_loanss)} Other_loans objects")
		#	orchestration.track_data_processing("Other_loans", self.Other_loanss, self.Other_loanss)
		
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table:
	LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT_Table = None 
	SCRTY_ENTTY_RL_ASSGNMNT_Table = None 
	ENTTY_RL_Table = None 
	SCRTY_EXCHNG_TRDBL_DRVTV_Table = None 
	LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT_Table = None 
	LNG_SHRT_BLNC_SHT_RCGNSD_SCRTY_PSTN_Table = None 
	BLNC_SHT_RCGNSD_NN_BLNC_SHT_RCGNSD_SCRTY_PSTN_Table = None 
	SCRTY_PSTN_Table = None 
	SCRTY_EXCHNG_TRDBL_DRVTV_Table = None 
	PRTY_Table = None 
	Non_Negotiable_bondss = []# Non_Negotiable_bonds[]
	@lineage(dependencies={"LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT.theLNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT",
		"LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT.theLNG_SHRT_BLNC_SHT_RCGNSD_SCRTY_PSTN",
		"LNG_SHRT_BLNC_SHT_RCGNSD_SCRTY_PSTN.theBLNC_SHT_RCGNSD_NN_BLNC_SHT_RCGNSD_SCRTY_PSTN",		
		"BLNC_SHT_RCGNSD_NN_BLNC_SHT_RCGNSD_SCRTY_PSTN.thetheSCRTY_PSTNPRTY",
		"SCRTY_PSTN.INSTRMNT_uniqtheSCRTY_EXCHNG_TRDBL_DRVTVueID",
		"SCRTY_EXCHNG_TRDBL_DRVTV.SCRTY_EXCHNG_TRDBL_DRVTV_uniqueID",
		"SCRTY_ENTTY_RL_ASSGNMNT.theENTTY_RL",
		"ENTTY_RL.thePRTY"
		})
	def calc_Non_Negotiable_bondss(self) :

		items = [] # Non_Negotiable_bonds[
		for long_Security_accntng_classification in self.LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT_Table:
			long_Security_assignment = long_Security_accntng_classification.theLNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ASSGNMNT
			lng_shrt_blnc_sht_rcgnsd_scrty_pstn = long_Security_assignment.theLNG_SHRT_BLNC_SHT_RCGNSD_SCRTY_PSTN
			blnc_sht_rcgnsd_nn_blnc_sht_rcgnsd_scrty_pstn = lng_shrt_blnc_sht_rcgnsd_scrty_pstn.theBLNC_SHT_RCGNSD_NN_BLNC_SHT_RCGNSD_SCRTY_PSTN
			scrty_pstn = blnc_sht_rcgnsd_nn_blnc_sht_rcgnsd_scrty_pstn.theSCRTY_PSTN
			scrty_exchng_trdbl_drvtv = scrty_pstn.theSCRTY_EXCHNG_TRDBL_DRVTV	
			
			
			new_item = Non_Negotiable_bonds()

			for scrty_entty_rl_assignment in self.SCRTY_ENTTY_RL_ASSGNMNT_Table:
				if scrty_entty_rl_assignment.theSCRTY_EXCHNG_TRDBL_DRVTV.SCRTY_EXCHNG_TRDBL_DRVTV_uniqueID == scrty_exchng_trdbl_drvtv.SCRTY_EXCHNG_TRDBL_DRVTV_uniqueID:
					new_item.SCRTY_ENTTY_RL_ASSGNMNT = scrty_entty_rl_assignment
					entty_rl = scrty_entty_rl_assignment.theENTTY_RL
					prty = entty_rl.thePRTY
					new_item.PRTY = prty
					break
			
			new_item.LNG_BLNC_SHT_RCGNSD_SCRTY_PSTN_PRDNTL_PRTFL_ACCNTNG_CLSSFCTN_ASSGNMNT = long_Security_accntng_classification
			new_item.LNG_SHRT_BLNC_SHT_RCGNSD_SCRTY_PSTN = lng_shrt_blnc_sht_rcgnsd_scrty_pstn
			new_item.BLNC_SHT_RCGNSD_NN_BLNC_SHT_RCGNSD_SCRTY_PSTN = blnc_sht_rcgnsd_nn_blnc_sht_rcgnsd_scrty_pstn
			new_item.SCRTY_PSTN = scrty_pstn
			new_item.SCRTY_EXCHNG_TRDBL_DRVTV = scrty_exchng_trdbl_drvtv
			items.append(new_item)
		return items
	
	@track_table_init
	def init(self):
		Orchestration().init(self)
		self.Non_Negotiable_bondss = []
		self.Non_Negotiable_bondss.extend(self.calc_Non_Negotiable_bondss())
		
		
		CSVConverter.persist_object_as_csv(self,True)
		return None

class F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table:
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_ENTTY_RL_ASSGNMNT_Table = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	PRTY_Table = None # PRTY
	Advances_that_are_not_loanss = []# Advances_that_are_not_loans[]
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theINSTRMNT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theENTTY_RL",		
		"ENTTY_RL.thePRTY",
		"INSTRMNT.INSTRMNT_uniqueID",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.INSTRMNT_ENTTY_RL_ASSGNMNT_uniqueID",
		"PRTY.PRTY_uniqueID",
		"INSTRMNT_RL.theINSTRMNT"
		})
	def calc_Advances_that_are_not_loanss(self) :
		items = [] # 
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		
		for instrmnt_rl in self.INSTRMNT_RL_Table:
			typeInst = instrmnt_rl.theINSTRMNT.INSTRMNT_TYP_PRDCT

			if (typeInst == '130') or (typeInst == '120') or (typeInst == '140'):
				
				newItem = Advances_that_are_not_loans()
				newItem.INSTRMNT_RL = instrmnt_rl
				newItem.INSTRMNT = instrmnt_rl.theINSTRMNT
				
				for era in  self.INSTRMNT_ENTTY_RL_ASSGNMNT_Table:
					inst = era.theINSTRMNT
					if (inst == newItem.INSTRMNT):
						newItem.INSTRMNT_ENTTY_RL_ASSGNMNT = era
						er = era.theENTTY_RL
						newItem.PRTY = er.thePRTY
					
				items.append(newItem)
	
		return items
	@track_table_init
	def init(self):
		Orchestration().init(self)
		self.Advances_that_are_not_loanss = []
		self.Advances_that_are_not_loanss.extend(self.calc_Advances_that_are_not_loanss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_05_01_REF_FINREP_3_0_Credit_card_debt_Table:
	CLLTRL_Table = None # CLLTRL
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_ENTTY_RL_ASSGNMNT_Table = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	PRTY_Table = None # PRTY
	Credit_card_debts = []# Credit_card_debt[]

	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theINSTRMNT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theENTTY_RL",		
		"ENTTY_RL.thePRTY",
		"INSTRMNT.INSTRMNT_uniqueID",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.INSTRMNT_ENTTY_RL_ASSGNMNT_uniqueID",
		"PRTY.PRTY_uniqueID",
		"INSTRMNT_RL.theINSTRMNT"
		})
	def calc_Credit_card_debts(self) :
		items = [] # 
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		
		for instrmnt_rl in self.INSTRMNT_RL_Table:
			typeInst = instrmnt_rl.theINSTRMNT.INSTRMNT_TYP_PRDCT
			#if (typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['140']) or \
			#		(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['1022'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['51'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['80'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['12'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['522'] ):
			if (typeInst == '51' ):
				
				newItem = Credit_card_debt()
				newItem.INSTRMNT_RL = instrmnt_rl
				newItem.INSTRMNT = instrmnt_rl.theINSTRMNT
				
				for era in  self.INSTRMNT_ENTTY_RL_ASSGNMNT_Table:
					inst = era.theINSTRMNT
					if (inst == newItem.INSTRMNT):
						newItem.INSTRMNT_ENTTY_RL_ASSGNMNT = era
						er = era.theENTTY_RL
						newItem.PRTY = er.thePRTY
					
				items.append(newItem)
	
		return items
	def init(self):
		Orchestration().init(self)
		self.Credit_card_debts = []
		self.Credit_card_debts.extend(self.calc_Credit_card_debts())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_05_01_REF_FINREP_3_0_Finance_leases_Table:
	CLLTRL_Table = None # CLLTRL
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_ENTTY_RL_ASSGNMNT_Table = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	PRTY_Table = None # PRTY
	Finance_leasess = []# Finance_leases[]
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theINSTRMNT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theENTTY_RL",		
		"ENTTY_RL.thePRTY",
		"INSTRMNT.INSTRMNT_uniqueID",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.INSTRMNT_ENTTY_RL_ASSGNMNT_uniqueID",
		"PRTY.PRTY_uniqueID",
		"INSTRMNT_RL.theINSTRMNT"
		})
	def calc_Finance_leasess(self) :
		items = [] # 
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		
		for instrmnt_rl in self.INSTRMNT_RL_Table:
			typeInst = instrmnt_rl.theINSTRMNT.INSTRMNT_TYP_PRDCT
			#if (typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['140']) or \
			#		(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['1022'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['51'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['80'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['12'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['522'] ):
			if (typeInst == '80' ):
				
				newItem = Finance_leases()
				newItem.INSTRMNT_RL = instrmnt_rl
				newItem.INSTRMNT = instrmnt_rl.theINSTRMNT
				
				for era in  self.INSTRMNT_ENTTY_RL_ASSGNMNT_Table:
					inst = era.theINSTRMNT
					if (inst == newItem.INSTRMNT):
						newItem.INSTRMNT_ENTTY_RL_ASSGNMNT = era
						er = era.theENTTY_RL
						newItem.PRTY = er.thePRTY
					
				items.append(newItem)
	
		return items
	def init(self):
		Orchestration().init(self)
		self.Finance_leasess = []
		self.Finance_leasess.extend(self.calc_Finance_leasess())
		CSVConverter.persist_object_as_csv(self,True)
		return None

class F_05_01_REF_FINREP_3_0_Trade_receivables_Table:
	CLLTRL_Table = None # CLLTRL
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_ENTTY_RL_ASSGNMNT_Table = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	PRTY_Table = None # PRTY
	Other_loanss = []# Other_loans[]	
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theINSTRMNT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theENTTY_RL",		
		"ENTTY_RL.thePRTY",
		"INSTRMNT.INSTRMNT_uniqueID",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.INSTRMNT_ENTTY_RL_ASSGNMNT_uniqueID",
		"PRTY.PRTY_uniqueID",
		"INSTRMNT_RL.theINSTRMNT"
		})
	def calc_Trade_receivabless(self) :
		items = [] # Other_loans[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		
		for instrmnt_rl in self.INSTRMNT_RL_Table:
			typeInst = instrmnt_rl.theINSTRMNT.INSTRMNT_TYP_PRDCT
			#if (typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['140']) or \
			#		(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['1022'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['51'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['80'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['12'] ) or \
			#	(typeInst == INSTRMNT.INSTRMNT_TYP_PRDCT_INPT_domain['522'] ):
			if (typeInst == '1023' ):
				
				newItem = Trade_receivables()
				newItem.INSTRMNT_RL = instrmnt_rl
				newItem.INSTRMNT = instrmnt_rl.theINSTRMNT
				
				for era in  self.INSTRMNT_ENTTY_RL_ASSGNMNT_Table:
					inst = era.theINSTRMNT
					if (inst == newItem.INSTRMNT):
						newItem.INSTRMNT_ENTTY_RL_ASSGNMNT = era
						er = era.theENTTY_RL
						newItem.PRTY = er.thePRTY
					
				items.append(newItem)
	
		return items
	def init(self):
		Orchestration().init(self)
		self.Trade_receivabless = []
		self.Trade_receivabless.extend(self.calc_Trade_receivabless())
		CSVConverter.persist_object_as_csv(self,True)
		return None

class F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table:
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_ENTTY_RL_ASSGNMNT_Table = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	PRTY_Table = None # PRTY
	On_demand_and_short_notices = []# On_demand_and_short_notice[]
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theINSTRMNT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theENTTY_RL",		
		"ENTTY_RL.thePRTY",
		"INSTRMNT.INSTRMNT_uniqueID",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.INSTRMNT_ENTTY_RL_ASSGNMNT_uniqueID",
		"PRTY.PRTY_uniqueID",
		"INSTRMNT_RL.theINSTRMNT"
		})
	def calc_On_demand_and_short_notices(self) :
		items = [] # On_demand_and_short_notice
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		
		for instrmnt_rl in self.INSTRMNT_RL_Table:
			typeInst = instrmnt_rl.theINSTRMNT.INSTRMNT_TYP_PRDCT
			if (typeInst == '511' ) or (typeInst == '522' ):
				newItem = On_demand_and_short_notice()
				newItem.INSTRMNT_RL = instrmnt_rl
				newItem.INSTRMNT = instrmnt_rl.theINSTRMNT
				
				for era in  self.INSTRMNT_ENTTY_RL_ASSGNMNT_Table:
					inst = era.theINSTRMNT
					if (inst == newItem.INSTRMNT):
						newItem.INSTRMNT_ENTTY_RL_ASSGNMNT = era
						er = era.theENTTY_RL
						newItem.PRTY = er.thePRTY
					
				items.append(newItem)
	
		return items
	def init(self):
		Orchestration().init(self)
		self.On_demand_and_short_notices = []
		self.On_demand_and_short_notices.extend(self.calc_On_demand_and_short_notices())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table:
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_ENTTY_RL_ASSGNMNT_Table = None # INSTRMNT_ENTTY_RL_ASSGNMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	PRTY_Table = None # PRTY
	Reverse_repurchase_agreementss = []# Reverse_repurchase_agreements[]
	@lineage(dependencies={"INSTRMNT.INSTRMNT_TYP_PRDCT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theINSTRMNT",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.theENTTY_RL",		
		"ENTTY_RL.thePRTY",
		"INSTRMNT.INSTRMNT_uniqueID",
		"INSTRMNT_ENTTY_RL_ASSGNMNT.INSTRMNT_ENTTY_RL_ASSGNMNT_uniqueID",
		"PRTY.PRTY_uniqueID",
		"INSTRMNT_RL.theINSTRMNT"
		})
	def calc_Reverse_repurchase_agreementss(self) :
		items = [] # On_demand_and_short_notice
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		
		for instrmnt_rl in self.INSTRMNT_RL_Table:
			typeInst = instrmnt_rl.theINSTRMNT.INSTRMNT_TYP_PRDCT
			if (typeInst == '1003' ) :
				newItem = Reverse_repurchase_agreements()
				newItem.INSTRMNT_RL = instrmnt_rl
				newItem.INSTRMNT = instrmnt_rl.theINSTRMNT
				
				for era in  self.INSTRMNT_ENTTY_RL_ASSGNMNT_Table:
					inst = era.theINSTRMNT
					if (inst == newItem.INSTRMNT):
						newItem.INSTRMNT_ENTTY_RL_ASSGNMNT = era
						er = era.theENTTY_RL
						newItem.PRTY = er.thePRTY
					
				items.append(newItem)
	
		return items
	def init(self):
		Orchestration().init(self)
		self.Reverse_repurchase_agreementss = []
		self.Reverse_repurchase_agreementss.extend(self.calc_Reverse_repurchase_agreementss())
		CSVConverter.persist_object_as_csv(self,True)
		return None

