******************************************************************************
******************************************************************************
**  Template file for TargetLink Custom Code blocks' custom code file
**
**  DESCRIPTION
**
**  This file contains code sections of a Custom Code block for
**   - floating-point simulations with Simulink
**   - production code simulations with Simulink
**   - production code simulations on the target microcontroller
**
**  The code sections between the keywords "flp_XXXX_begin" and "flp_XXXX_end"
**  are automatically inserted into the S-function, which represents the
**  Custom Code block in floating-point simulations.
**
**  The code sections between the keywords "fxp_XXXX_begin" and "fxp_XXXX_end"
**  are inserted by TargetLink into the generated production C code file for
**  the model.
**
**  If the option "Use production code for floating-point simulation" is
**  enabled in the Custom Code block dialog, the fxp_XXX sections will be used
**  for floating-point simulations also. In this case there is no need to
**  specify the flp_XXX sections.
**
**  The following code sections are supported:
**
**    .._decl_..       Code to perform declarations for the Custom Code block
**                      - inclusion of header files (you may as well use
**                        Addfile blocks for this)
**                      - variable declarations
**                      - preprocessor defines
**
**    .._header_..     Code to be placed in the header file
**                     
**    .._restart_..    Restart statements to be executed when the application
**                     is started
**                      - initialize I/O devices
**
**    .._init_..       Initialization statements to be executed when the states
**                     are reset, for example, for enabled subsystems
**                      - set initial values of state variables
**
**    .._output_..     Compute the outputs of the Custom block
**
**    .._update_..     Update operations performed at the end of a computation
**                     step
**                      - update discrete state variables
**
**    .._terminate_..  Code to be executed when the simulation is stopped
**                      - clear I/O devices
**
**  Additionally, you can add keywords to every code section. The syntax is
** 
**    <section>(<keywords>)
**  
**  for example
**   
**    fxp_<section>_begin(top,common)
**        
**  The following keywords are supported:
**
**  top          the code is inserted topmost in the generated code
**                - I/O code which must be performed first, independantly
**                  from the execution order of the model     
**                
**  bottom       the code is inserted bottommost   
**
**  common       only one instance of the code is inserted for all instances
**               of the associated custom code block.
**
**
**  If you use keywords, you can have code sections which differ only by their
**  keywords, for example two .._output_.. sections, one with the keyword top,
**  the other one with the keyword bottom.
**  
**  Unused code modules may be deleted if you use this file as a template.
**
**  Everything outside of the code modules marked with xx_begin ... xx_end
**  will be treated as a comment and ignored.
**  
**  $Workfile:   L2Config_template_d2gu.c  $ $Revision:   1.1  $ $Date:   Apr 08 2019 14:14:40  $
**  $Archive:   E:/PVCS_Root/PVCSdatMEG/DCT2x/archives/DCT2x_TL42/Funct_tl/L2/L2Config_template_d2gu.c-arc  $
**  author:   U. Kiffmeier, dSPACE GmbH
******************************************************************************
******************************************************************************


##############################################################################
# Enter header code for floating-point simulation below
##############################################################################
/* flp_header_begin */

/* flp_header_end */


##############################################################################
# Enter header code for production code simulation below
##############################################################################
/* fxp_header_begin */
#ifdef MOD_NR_MODUL
    #undef MOD_NR_MODUL
    #define MOD_NR_MODUL module_id
#else
   #define MOD_NR_MODUL module_id
#endif

/* fxp_header_end */


##############################################################################
# Enter declaration code for floating-point simulation below
##############################################################################
/* flp_decl_begin */

/* flp_decl_end */


##############################################################################
# Enter declaration code for production code simulation below
##############################################################################
/* fxp_decl_begin */

/* fxp_decl_end */


##############################################################################
# Enter restart code for floating-point simulation below
# (executed when the application is (re-)started)
##############################################################################
/* flp_restart_begin */

/* flp_restart_end */


##############################################################################
# Enter restart code for production code simulation below
# (executed when the application is (re-)started)
##############################################################################
/* fxp_restart_begin */
#ifndef TL_FRAME
    /*setMonPfcStepInitL2_MTSP(1, 5, progStart);*/
    /*setMonPfcStepInitL2_MTSP(1, 5, progStop);*/
#endif

/* fxp_restart_end */


##############################################################################
# Enter initialization code for floating-point simulation below
# (executed when states are re-initialized for enabled subsystems)
##############################################################################
/* flp_init_begin */

/* flp_init_end */


##############################################################################
# Enter initialization code for production code simulation below
# (executed when states are re-initialized for enabled subsystems)
##############################################################################
/* fxp_init_begin */

/* fxp_init_end */


##############################################################################
# Enter output vector evaluation code for floating-point simulation below
##############################################################################
/* flp_output_begin */

/* flp_output_end */


##############################################################################
# Enter output vector evaluation code for production code simulation below
##############################################################################
/* fxp_output_begin(top) */
#ifndef TL_FRAME
     /*setMonPfcStepL2_MTSP(1, 5, progStart);*/
#endif
/* fxp_output_end(top) */
/* fxp_output_begin(bottom) */
#ifndef TL_FRAME
     /*setMonPfcStepL2_MTSP(1, 5, progStop);*/   
#endif
/* fxp_output_end(bottom) */


##############################################################################
# Enter update code for floating-point simulation below
##############################################################################
/* flp_update_begin */

/* flp_update_end */


##############################################################################
# Enter update code for production code simulation below
##############################################################################
/* fxp_update_begin */

/* fxp_update_end */


##############################################################################
# Enter terminate code for floating-point simulation below
##############################################################################
/* flp_terminate_begin */
   
/* flp_terminate_end */


##############################################################################
# Enter terminate code for production code simulation below
##############################################################################
/* fxp_terminate_begin */

/* fxp_terminate_end */
