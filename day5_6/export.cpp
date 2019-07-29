#include <pybind11/pybind11.h>
#include <pybind11/stl.h> // standard library
#include <pybind11/eigen.h> // for matrix
#include "hello_world.hpp"

PYBIND11_MODULE(sss_cpp, m)
{
	m.doc() = "This is an example C++ module called from python";
	m.def("f_to_celsius", f_to_celsius, "Convert fahrenheit to celsius");
	m.def("c_to_k", c_to_k, "Convert celsius to kelvin");
	m.def("f_to_kelvin", f_to_kelvin, "Convert ahrenheit to kelvin");
	m.def("check_temperature", check_temperature, "Check if the temperature is unphysical");
	m.def("count", count, "Print the count up to a given number");
	m.def("f_to_c_vector", f_to_c_vector, "Convert a vector of fahrenheit to celsius");
	m.def("f_to_c_matrix", f_to_c_matrix, "Convert a matrix of fahrenheit to celsius");
	// 1) function name in Python 2) function name in c++ 3) string to describe function 
}
