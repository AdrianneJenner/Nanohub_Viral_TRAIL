/*
###############################################################################
# If you use PhysiCell in your project, please cite PhysiCell and the version #
# number, such as below:                                                      #
#                                                                             #
# We implemented and solved the model using PhysiCell (Version x.y.z) [1].    #
#                                                                             #
# [1] A Ghaffarizadeh, R Heiland, SH Friedman, SM Mumenthaler, and P Macklin, #
#     PhysiCell: an Open Source Physics-Based Cell Simulator for Multicellu-  #
#     lar Systems, PLoS Comput. Biol. 14(2): e1005991, 2018                   #
#     DOI: 10.1371/journal.pcbi.1005991                                       #
#                                                                             #
# See VERSION.txt or call get_PhysiCell_version() to get the current version  #
#     x.y.z. Call display_citations() to get detailed information on all cite-#
#     able software used in your PhysiCell application.                       #
#                                                                             #
# Because PhysiCell extensively uses BioFVM, we suggest you also cite BioFVM  #
#     as below:                                                               #
#                                                                             #
# We implemented and solved the model using PhysiCell (Version x.y.z) [1],    #
# with BioFVM [2] to solve the transport equations.                           #
#                                                                             #
# [1] A Ghaffarizadeh, R Heiland, SH Friedman, SM Mumenthaler, and P Macklin, #
#     PhysiCell: an Open Source Physics-Based Cell Simulator for Multicellu-  #
#     lar Systems, PLoS Comput. Biol. 14(2): e1005991, 2018                   #
#     DOI: 10.1371/journal.pcbi.1005991                                       #
#                                                                             #
# [2] A Ghaffarizadeh, SH Friedman, and P Macklin, BioFVM: an efficient para- #
#     llelized diffusive transport solver for 3-D biological simulations,     #
#     Bioinformatics 32(8): 1256-8, 2016. DOI: 10.1093/bioinformatics/btv730  #
#                                                                             #
###############################################################################
#                                                                             #
# BSD 3-Clause License (see https://opensource.org/licenses/BSD-3-Clause)     #
#                                                                             #
# Copyright (c) 2015-2018, Paul Macklin and the PhysiCell Project             #
# All rights reserved.                                                        #
#                                                                             #
# Redistribution and use in source and binary forms, with or without          #
# modification, are permitted provided that the following conditions are met: #
#                                                                             #
# 1. Redistributions of source code must retain the above copyright notice,   #
# this list of conditions and the following disclaimer.                       #
#                                                                             #
# 2. Redistributions in binary form must reproduce the above copyright        #
# notice, this list of conditions and the following disclaimer in the         #
# documentation and/or other materials provided with the distribution.        #
#                                                                             #
# 3. Neither the name of the copyright holder nor the names of its            #
# contributors may be used to endorse or promote products derived from this   #
# software without specific prior written permission.                         #
#                                                                             #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" #
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE   #
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE  #
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE   #
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR         #
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF        #
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS    #
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN     #
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)     #
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE  #
# POSSIBILITY OF SUCH DAMAGE.                                                 #
#                                                                             #
###############################################################################
*/

#include "./Epil_virus_veins.h"
#include "../modules/PhysiCell_settings.h"

Cell_Definition vein_wall_cell;

void create_vein_wall_cell( void )
{
	//initialize_default_cell_definition();
	vein_wall_cell = cell_defaults;
	
	vein_wall_cell.name = "vein_wall_cell";
	vein_wall_cell.type = 1;
	
	// set virus secretion rates from vein wall cells
	vein_wall_cell.phenotype.secretion.secretion_rates[1] = 0;
	vein_wall_cell.phenotype.secretion.uptake_rates[1] = 0;
	vein_wall_cell.phenotype.secretion.saturation_densities[1] = 10; 
	
	// stopping these cells from updating their phenotype
	vein_wall_cell.functions.update_phenotype = intravenous_injection_saturation; 
	
	int cycle_start_index = live.find_phase_index( PhysiCell_constants::live ); 
	int cycle_end_index = live.find_phase_index( PhysiCell_constants::live ); 
	vein_wall_cell.phenotype.cycle.data.transition_rate( cycle_start_index , cycle_end_index ) = 0.0; 
	
	vein_wall_cell.phenotype.motility.is_motile = false; 
	
	return;
}

void create_cell_types( void )
{
	// housekeeping 
	SeedRandom( parameters.ints( "random_seed" ) ); 
	initialize_default_cell_definition();	
	
	//setting cycle model to live
	cell_defaults.phenotype.cycle.sync_to_cycle_model( live ); 
	
	
	// Make sure we're ready for 2D
	cell_defaults.functions.set_orientation = up_orientation;  
	cell_defaults.phenotype.geometry.polarity = 1.0; 
	cell_defaults.phenotype.motility.restrict_to_2D = true; 


	cell_defaults.phenotype.secretion.sync_to_microenvironment( &microenvironment );
	
    // turn off proliferation 
	//int cycle_start_index = live.find_phase_index( PhysiCell_constants::live ); 
	//int cycle_end_index = live.find_phase_index( PhysiCell_constants::live ); 
	//cell_defaults.phenotype.cycle.data.transition_rate( cycle_start_index , cycle_end_index ) = 0.0; 
	
	// turn off death
	int apoptosis_index = cell_defaults.phenotype.death.find_death_model_index( PhysiCell_constants::apoptosis_death_model ); 
	cell_defaults.phenotype.death.rates[apoptosis_index] = 0.0; 
	
	// add variables to track virus infection start time, length of time and amount of virus
	cell_defaults.custom_data.add_variable( "intracellular_virus_amount", "dimensionless", 0.0 );
	cell_defaults.custom_data.add_variable( "infection_time_start", "dimensionless", -1.0 );
	cell_defaults.custom_data.add_variable( "infection_time_length", "dimensionless", -1.0 );
	cell_defaults.custom_data.add_variable( "time_of_injection", "dimensionless", 0.0 );
	
	std::vector<double> namekk(3);
	namekk = {0,100,200};
	std::cout<<namekk<<std::endl;
	cell_defaults.custom_data.add_vector_variable( "time_of_injections", "dimensionless", namekk );
	
	// turn off secretion from these cells (oxygen and virus)
	cell_defaults.phenotype.secretion.secretion_rates[0] = 0;
	cell_defaults.phenotype.secretion.uptake_rates[0] = 0;
	cell_defaults.phenotype.secretion.saturation_densities[0] = 40; 
		
	cell_defaults.phenotype.secretion.secretion_rates[1] = 0;
	cell_defaults.phenotype.secretion.uptake_rates[1] = 0;
	cell_defaults.phenotype.secretion.saturation_densities[1] = 10; 
	
	// update cell and phenotype based on virus dynamics only
	cell_defaults.functions.update_phenotype = virus_dynamics_new; 
	//cell_defaults.functions.custom_cell_rule = virus_dynamics; 
	
	cell_defaults.phenotype.motility.is_motile = true; 
	
	create_vein_wall_cell();
	
	return; 
}

void setup_microenvironment( void )
{
	// set domain parameters

	// now this is in XML 
	default_microenvironment_options.X_range = {-1000, 1000}; 
	default_microenvironment_options.Y_range = {-1000, 1000}; 
	default_microenvironment_options.simulate_2D = true; 
		
	// make sure not override and go back to 2D 
	if( default_microenvironment_options.simulate_2D == false )
	{
		std::cout << "Warning: overriding XML config option and setting to 2D!" << std::endl; 
		default_microenvironment_options.simulate_2D = true; 
	}
	
	// chemoattractant gradient needed	
	default_microenvironment_options.calculate_gradients = true; 
	
	// setting oxygen diffusion parameters
	microenvironment.diffusion_coefficients[0] = 1e2; 
	microenvironment.decay_rates[0] = 0; 
	
	// add virus
	microenvironment.add_density( "virus", "dimensionless" ); 
	microenvironment.diffusion_coefficients[1] = 1e1; 
	microenvironment.decay_rates[1] = 0.001; 
	
	// let BioFVM use oxygen as the default 
	default_microenvironment_options.use_oxygen_as_first_field = true; 
	

	// set Dirichlet conditions 
	default_microenvironment_options.outer_Dirichlet_conditions = true;
	default_microenvironment_options.Dirichlet_condition_vector[0] = 40; // normoxic conditions 
	default_microenvironment_options.outer_Dirichlet_conditions = true;
	default_microenvironment_options.Dirichlet_condition_vector[1] = 0; // normoxic conditions 
	
	initialize_microenvironment(); 	

	
	// any custom initial profiles  go here 
	
	/*for( int n = 0 ; n < microenvironment.mesh.voxels.size(); n++ )
	{	
	
	}
	*/
	return; 
}	

void setup_tissue( void )
{
	double start_of_boundary = -1000;
	double start_of_xboundary = start_of_boundary*2/sqrt(3);
	double end_of_boundary = 1000;
	double no_of_points_in_yline = (end_of_boundary-start_of_boundary)/18;
	
	
	double no_of_points_in_xline = 2*(end_of_boundary-start_of_boundary)/18/sqrt(3);
	
	Cell* pCell = NULL; 
	
	double x = 0.0;
	double y = 0.0;
	
	double xgrid = 0.0;
	double ygrid = 0.0;
	
	//placing vien cells and normal cells in a hexagonal grid
	for( int i=0; i<no_of_points_in_xline; i++ )
	{	
		xgrid = start_of_xboundary+i*18;
		x = sqrt(3)/2*xgrid;
		
		for( int j=0; j<no_of_points_in_yline; j++ )
		{
			ygrid = start_of_boundary+j*18;
			if( i % 2 == 0 )
			{y = ygrid+6;}
			else
			{y = ygrid;}
			
			if ( x>start_of_boundary && x<0 && y<x-10&&y>2*x-10)
			{pCell = create_cell( vein_wall_cell );
			pCell->is_movable = false;}
			else if (  x>50 && x<180 && y<495/10*(x-50)+5 && y>495/130*(x-50)+5 ) 
			{pCell = create_cell( vein_wall_cell );
			pCell->is_movable = false;}
			else
			{pCell = create_cell(  );}
		
			pCell->assign_position( x , y , 0.0 );
			
		}
		
	}

	return;
	
}
/*
void virus_dynamics( Cell* pCell, Phenotype& phenotype, double dt )
{
	
	// virus parameters
	double virus_min = 0.1;
	double viral_progeny = 20;
	double length_of_infect = 150;
	
	// find virus index
	static int virus_signal_index	= microenvironment.find_density_index( "virus" ); 
	static int apoptosis_model_index =
		pCell->phenotype.death.find_death_model_index( "apoptosis" );
	
	// sample amount of virus
	double virus_amount = pCell->nearest_density_vector()[virus_signal_index];
	
	static double infection_time_length_index = pCell->custom_data.find_variable_index( "infection_time_length" );	
	static double intracellular_virus_index = pCell->custom_data.find_variable_index( "intracellular_virus_amount" );
	static double infection_time_start_index = pCell->custom_data.find_variable_index( "infection_time_start" );	
	
	static double infection_density_capacity = parameters.doubles("infection_density_capacity");
	static double intrinsic_infection_rate = parameters.doubles("intrinsic_infection_rate"); //2; 
	static double viral_replication_rate = parameters.doubles("viral_replication_rate");	
	
	if( pCell->phenotype.death.dead==true)
	{std::cout<<"is dead"<<std::endl;}
	if( pCell->custom_data.variables[infection_time_start_index].value < 0 && virus_amount>virus_min && pCell->phenotype.death.dead==false && PhysiCell_globals.current_time >0)
	{
		// infection occurs
		pCell->custom_data.variables[infection_time_start_index].value = PhysiCell_globals.current_time;
		pCell->custom_data.variables[infection_time_length_index].value = dt;
		
		double K = infection_density_capacity;
		double beta = intrinsic_infection_rate;
		double tstar = PhysiCell_globals.current_time;
		double I_V = pCell->custom_data.variables[intracellular_virus_index].value;
		double A = exp(beta*virus_amount*tstar/K)*(1-I_V/K);
		double kappa =  viral_replication_rate;
		
		pCell->custom_data.variables[intracellular_virus_index].value = K*(1-A*exp(-beta*virus_amount/K*(tstar+dt)));// function WITHOUT replication
		//pCell->custom_data.variables[intracellular_virus_index].value =  = I_V+dt*(beta*virus_amount*(1-I_V/K)+kappa*I_V*(1-I_V/K));// function WITH replication
		
		pCell->phenotype.secretion.uptake_rates[virus_signal_index] = beta*virus_amount*(1-I_V/K);
	}
	else if( pCell->custom_data.variables[infection_time_start_index].value > 0 && pCell->custom_data.variables[infection_time_length_index].value < length_of_infect)
	{
		// infection ongoing
		pCell->custom_data.variables[infection_time_length_index].value = PhysiCell_globals.current_time-pCell->custom_data.variables[infection_time_start_index].value;
		
		// make uptake rate a function of time since first uptake and also maximum capacity
		double K = infection_density_capacity;
		double beta = intrinsic_infection_rate;
		double tstar = PhysiCell_globals.current_time;
		double I_V = pCell->custom_data.variables[intracellular_virus_index].value;
		double A = exp(beta*virus_amount*tstar/K)*(1-I_V/K);
		double kappa =  viral_replication_rate;
		
		//pCell->custom_data.variables[intracellular_virus_index].value = K*(1-A*exp(-beta*virus_amount/K*(tstar+dt)));// function WITHOUT replication
		pCell->custom_data.variables[intracellular_virus_index].value = I_V+dt*(beta*virus_amount*(1-I_V/K)+kappa*I_V*(1-I_V/K));// function WITH replication
		pCell->phenotype.secretion.uptake_rates[virus_signal_index] = beta*virus_amount*(1-I_V/K); 
		
	}
	else if( pCell->custom_data.variables[infection_time_length_index].value > length_of_infect )
	{
		// cell lyse
		pCell->custom_data.variables[infection_time_start_index].value = -1;
		pCell->custom_data.variables[infection_time_length_index].value = -1;
		pCell->start_death( apoptosis_model_index );
		pCell->phenotype.secretion.secretion_rates[virus_signal_index] = 10;//viral_progeny/dt;
		pCell->phenotype.secretion.uptake_rates[virus_signal_index] = 0;
	}
	
	
	return;
}*/

void virus_dynamics_new( Cell* pCell, Phenotype& phenotype, double dt )
{
	
	// find virus index
	static int virus_signal_index	= microenvironment.find_density_index( "virus" ); 
	
	// sample amount of virus
	double virus_amount = pCell->nearest_density_vector()[virus_signal_index];
	
	static double intracellular_virus_index = pCell->custom_data.find_variable_index( "intracellular_virus_amount" );
	
	static double infection_density_capacity = parameters.doubles("infection_density_capacity");
	static double intrinsic_infection_rate = parameters.doubles("intrinsic_infection_rate"); //2; 
	static double viral_replication_rate = parameters.doubles("viral_replication_rate");	
	static double virus_replication_minimum = parameters.doubles("virus_replication_minimum");	
	
	double c_I = intrinsic_infection_rate;//rate of infection
	double K = infection_density_capacity;//capacity of cell
	double c_R = viral_replication_rate;
	double n_Istar = virus_replication_minimum;
	double rho_E = virus_amount;
	int alpha = 1;
	double L = K/2+1.3*K/2;
	
	double V_voxel = microenvironment.mesh.voxels[1].volume;//volume of voxel
	
	double n_I = pCell->custom_data.variables[intracellular_virus_index].value;
	double n_E = virus_amount*V_voxel;

	if( pCell->phenotype.death.dead==false && virus_amount>1e-3)
	{
		if( n_I > n_Istar )
		{pCell->custom_data.variables[intracellular_virus_index].value = n_I+dt*(c_I*n_E*(1-n_I/K)+c_R);}
		else
		{pCell->custom_data.variables[intracellular_virus_index].value = n_I+dt*(c_I*n_E*(1-n_I/K));}

		n_I = pCell->custom_data.variables[intracellular_virus_index].value;
		pCell->phenotype.secretion.uptake_rates[virus_signal_index] = c_I*rho_E*(1-n_I/K);
		
		static int apoptosis_model_index =
			pCell->phenotype.death.find_death_model_index( "apoptosis" );
		
		if( n_I>0 && n_I<K/2 )
		{pCell->phenotype.death.rates[apoptosis_model_index] = 0.0;}
		else if( n_I>=K/2 && n_I<L )
		{pCell->phenotype.death.rates[apoptosis_model_index] = n_I*n_I*n_I/(L*L*L+n_I*n_I*n_I);}
		else
		{pCell->start_death( apoptosis_model_index );}// or cell enters apoptosis stage?}
	}
	else if( pCell->phenotype.death.dead==true)
	{
		pCell->phenotype.secretion.uptake_rates[virus_signal_index] = 0;
		pCell->phenotype.secretion.secretion_rates[virus_signal_index] = 0;		
		if( pCell->custom_data.variables[intracellular_virus_index].value>0)
			{
				double amount_in_cell = pCell->custom_data.variables[intracellular_virus_index].value;
				pCell->nearest_density_vector()[virus_signal_index] += amount_in_cell/V_voxel;
				pCell->custom_data.variables[intracellular_virus_index].value=0;
				pCell->phenotype.secretion.saturation_densities[virus_signal_index] = 5;
				
			}
		}

	return;
}


void intravenous_injection_saturation( Cell* pCell, Phenotype& phenotype, double dt )
{
	
	static int time_of_injections_index = pCell->custom_data.find_variable_index( "time_of_injections" );
	static double intracellular_virus_index = pCell->custom_data.find_variable_index( "intracellular_virus_amount" );
	static double s_V = parameters.doubles("secretion_rate_vein_wall_cell");
	static double  V_0 = parameters.doubles("no_of_viruses_in_initial_injection");
	
	std::vector<double> times = pCell->custom_data.vector_variables[time_of_injections_index].value;
	
	int no_of_injections = times.size();
	
	double V_voxel = microenvironment.mesh.voxels[1].volume;//volume of voxel
	double n_I = pCell->custom_data.variables[intracellular_virus_index].value; // amount of virus
	
	
	// are cells currently secreting
	if( pCell->phenotype.secretion.secretion_rates[1]>0 ) // if cells are currently secreting virus it means they still have some of the injection left to secrete
	{
		for( int i=0; i<no_of_injections; i++ ) // check whether new injection has occured
		{
			if(times[i]>=PhysiCell_globals.current_time&& times[i]<PhysiCell_globals.current_time+dt) //new injection occurs
			{
				//std::cout<<"Injection occured while another one was going on, time is "<<PhysiCell_globals.current_time<<std::endl;
				
				if(pCell->custom_data.variables[intracellular_virus_index].value>1) // if intracellular amount is still above some threshold (i.e. there is more than some minute amount left in the cell)
				{
					
					pCell->phenotype.secretion.secretion_rates[1] = 1/V_voxel*s_V*n_I;
					double n_I = pCell->custom_data.variables[intracellular_virus_index].value; // amount of virus
					pCell->custom_data.variables[intracellular_virus_index].value = n_I-dt*(s_V*n_I)+V_0;
					//std::cout<<"New injection whilst previous one is still going:  "<< pCell->phenotype.secretion.secretion_rates[1]<< " Intracellular amout: "<<pCell->custom_data.variables[intracellular_virus_index].value<<std::endl;
				
				}
				else
				{
					pCell->phenotype.secretion.secretion_rates[1] = 1/V_voxel*s_V*n_I;
					pCell->custom_data.variables[intracellular_virus_index].value = V_0;
					//std::cout<<"New injection:  "<< pCell->phenotype.secretion.secretion_rates[1]<< " Intracellular amout: "<<pCell->custom_data.variables[intracellular_virus_index].value<<std::endl;
				
				}
			}	 
			else // no new injection so keep reducing secretion rate
			{
				if(pCell->custom_data.variables[intracellular_virus_index].value>1) // if injection hasn't run out
				{
					
					pCell->custom_data.variables[intracellular_virus_index].value = n_I-dt*(s_V*n_I);
					double n_I = pCell->custom_data.variables[intracellular_virus_index].value; // amount of virus
					pCell->phenotype.secretion.secretion_rates[1] = 1/V_voxel*s_V*n_I;
					//std::cout<<"Injection still going:  "<< pCell->phenotype.secretion.secretion_rates[1]<< " Intracellular amout: "<<pCell->custom_data.variables[intracellular_virus_index].value<<std::endl;
				
				}
				else
				{
					
					pCell->phenotype.secretion.secretion_rates[1] = 0;
					pCell->custom_data.variables[intracellular_virus_index].value = 0;;
					pCell->phenotype.secretion.saturation_densities[1] = 3; 
					//std::cout<<"Injection has ended Secretion rate:  "<< pCell->phenotype.secretion.secretion_rates[1]<< " Intracellular amout: "<<pCell->custom_data.variables[intracellular_virus_index].value<<std::endl;
				
				}
			}
		}
	}
	else // check if an injection occurs
	{
		for( int i=0; i<no_of_injections; i++ ) // check whether new injection has occured
			{
				if(times[i]>=PhysiCell_globals.current_time&& times[i]<PhysiCell_globals.current_time+dt) //new injection occurs
				{
					std::cout<<"injection occurs"<<std::endl;
					pCell->custom_data.variables[intracellular_virus_index].value = V_0;
					double n_I = pCell->custom_data.variables[intracellular_virus_index].value; // amount of virus
					pCell->phenotype.secretion.secretion_rates[1] = 1/V_voxel*s_V*n_I;
				}
			}
	}
	
	return;
}

std::vector<std::string> colouring_by_cell_type_and_cycle( Cell* pCell )
{
	std::vector< std::string > output( 4, "darkgrey" ); 
	
	static int infection_time_index = pCell->custom_data.find_variable_index( "infection_time_length" );	
	static int intracellular_virus_index = pCell->custom_data.find_variable_index( "intracellular_virus_amount" );
	static int virus_signal_index	= microenvironment.find_density_index( "virus" ); 
	
	
	if( pCell->phenotype.death.dead == false && pCell->type == 0)
		{
			if( pCell->custom_data.variables[infection_time_index].value < 0 )
			{
				output[0] = "rgb(255, 182, 193)";
				output[1] = "rgb(255, 182, 193)";
				output[2] = "rgb(255, 160, 122)";
				output[3] = "rgb(255, 160, 122)";
				return output; 
			}
			else if( pCell->custom_data.variables[infection_time_index].value > 0 )
			{
				output[0] = "rgb(186, 85, 211)";
				output[1] = "rgb(186, 85, 211)";
				output[2] = "rgb(123, 104, 238)";
				output[3] = "rgb(123, 104, 238)";
				return output; 
			}
			else
			{
				std::cout<<"Problem "<<pCell->custom_data.variables[infection_time_index].value<< std::endl;
				 
				
			}
		}
	
	if( pCell->type == 1 )
	{
		
		output[0] = "red";
		output[1] = "red";
		output[2] = "red";
		output[3] = "red";
		return output; 
	}
	
	if( pCell->phenotype.death.dead == true )
	{ 
			output[0] = "rgb(255, 255, 224)";
			output[1] = "rgb(255, 255, 224)";
			output[2] = "rgb(255, 228, 181)";
			output[3] = "rgb(255, 228, 181)";
			
			std::cout<<"Plotting dead cell"<<std::endl;
		return output; 
	}
	
	return output;
}


std::vector<std::string> colouring_by_intracellular_virus_amount( Cell* pCell )
{
	
	// XXXXX COLORING BY INTRACELLULAR VIRUS 
	std::vector< std::string > output( 4, "darkgrey" ); 
	
	static int intracellular_virus_index = pCell->custom_data.find_variable_index( "intracellular_virus_amount" );
	static int infection_density_capacity = parameters.doubles("infection_density_capacity");
	
	double p_min = 1;
	double p_max = infection_density_capacity;
	static double  V_0 = parameters.doubles("no_of_viruses_in_initial_injection");
	
	
	double n_I = pCell->custom_data.variables[intracellular_virus_index].value; // amount of virus
	
	if( pCell->phenotype.death.dead==false && pCell->type==0)
	{
		int oncoprotein = (int) round( (1.0/(p_max-p_min)) * (pCell->custom_data.variables[intracellular_virus_index].value-p_min) * 255.0 ); 
		char szTempString [128]; // ceates a character array that can store 128
		sprintf( szTempString , "rgb(%u,%u,%u)", oncoprotein, oncoprotein, 255-oncoprotein ); // puts oncoprotein, oncoprotein and 255-oncoprotein in place of u u u
		
		
		if(pCell->custom_data.variables[intracellular_virus_index].value>1)
		{
			
			int oncoprotein = (int) round( (1.0/(p_min-p_max)) * (pCell->custom_data.variables[intracellular_virus_index].value-p_max) * 230.0 ); 
			char szTempString [128]; // ceates a character array that can store 128
			sprintf( szTempString , "rgb(%u,%u,%u)", oncoprotein, oncoprotein,255); // puts oncoprotein, oncoprotein and 255-oncoprotein in place of u u u
			output[0].assign( szTempString );
			output[1]="blue";
			output[2].assign( szTempString );
			output[3]="blue";
			//std::cout<<"oncoprotein: "<<oncoprotein<<". intracellular amount: "<<pCell->custom_data.variables[intracellular_virus_index].value<<std::endl;
			return output;
		}
	}
	
	if( pCell->type == 1 )
	{
		if( n_I > 0 )
		{
			double p_min = 1;
			double p_max = V_0;
			
			
			int oncoprotein = (int) round( (1.0/(p_min-p_max)) * (pCell->custom_data.variables[intracellular_virus_index].value-p_max) * 230.0 ); 
			char szTempString [128]; // ceates a character array that can store 128
			sprintf( szTempString , "rgb(%u,%u,%u)", 255, oncoprotein, oncoprotein); // puts oncoprotein, oncoprotein and 255-oncoprotein in place of u u u
			output[0].assign( szTempString );
			output[1]="red";
			output[2].assign( szTempString );
			output[3]="red";
			
			//std::cout<<"Time: "<< PhysiCell_globals.current_time << " intracelular amount: "<<pCell->custom_data.variables[intracellular_virus_index].value<<" oncoprotein: "<< oncoprotein<<std::endl;
			
			return output;
		}
		else
		{
				output[0] = "rgb(255,230,230)";
				output[1] = "red";
				output[2] = "rgb(255,230,230)";
				output[3] = "red";
				return output; 
		}
	}
	if( pCell->phenotype.death.dead == true )
	{ 
			output[0] = "rgb(255, 255, 224)";
			output[1] = "rgb(255, 255, 224)";
			output[2] = "rgb(255, 228, 181)";
			output[3] = "rgb(255, 228, 181)";
			
		
		return output; 
	}
	 
	return output;
}

