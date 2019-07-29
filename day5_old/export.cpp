#include <pybind11/pybind11.h>
#include "hello_world.hpp"

PYBIND11_MODULE(sss_cpp, m)
{
	m.doc() = "This is an example C++ module called from python";
	m.def("f_to_celsius", f_to_celsius, "Convert fahrenheit to celsius");
}
