#pragma once // include the header file for only once
#include <vector>
#include <Eigen/Dense>

double f_to_celsius(double f_temp);

double c_to_k(double c_temp);

double f_to_kelvin(double f_temp);

bool check_temperature(double f_temp);

void count(int max);

std::vector<double> f_to_c_vector(std::vector<double> f_vec);

Eigen::MatrixXd f_to_c_matrix(Eigen::MatrixXd f_mat);

