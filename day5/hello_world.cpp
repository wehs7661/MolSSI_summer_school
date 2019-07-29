#include <iostream> // just like importing a module in Python
/* Lines beginning with a hash sign (#) are directives read and interpreted by what is known as the preprocessor. 
 * They are special lines interpreted before the compilation of the program itself begins. In this case, the directive #include <iostream>, 
 * instructs the preprocessor to include a section of standard C++ code, known as header iostream, that allows to perform standard input and 
 * output operations, such as writing the output of this program (Hello World) to the screen.
 */
# include <vector>
# include <string>   // used for storing string variable (instead of just printing out)
# include <Eigen/Dense>
# include "hello_world.hpp"  // include the header file

/* double f_to_celsius(double f_temp)
{
	return (f_temp - 32.0)/1.8;
}*/

const double zero_k = 273.15;
double f_to_Kelvin(double f_temp) // use function as an input
{
	return (f_to_celsius(f_temp) + zero_k);
}

// Return false if f_temp is unphysical (below 0K)
bool check_temperature(double f_temp) 
{
	double k = f_to_Kelvin(f_temp);
	if(k <= 0)     // or if(k <= 0 || k > 1.0e6) and remove the else if statement below
		return false;
	else if(k > 1.0e6)
		return false;
	else 
		return true;
}

void count(int max)
{
	for(int i = 0; i < max; i++)
		std::cout << "i is " << i << std::endl;
}

void print_vector_1(std::vector<double> vec)  // a function for printing the elements of a vector 
{
	for(size_t i = 0; i < vec.size(); i++)   // vec.size() return a datay type called size_t, instead of int
		std::cout << "Method 1: elementes of pi_vector are " << vec[i] << std::endl;
}


void print_vector_2(std::vector<double> vec)  // another method
{
	// range-based for loop
	for(double it : vec)  // it: value inside the vector (colon means "in")
		std::cout << "Method 2: elementes of pi_vector are " << it <<std::endl;
}

int main(void)
{
	std::cout << "Hello, world!" << std::endl;  // std:: is the namespace
	std::cout << "This is Wei-Tse\n" << std::endl; // \n is an escape character (line feed)

	int a = 10;
	// int a = 5; will have an error like having a declared previously
	// float a = 5; we can not declare a as another datatype
	a = 1.8; // everyline should be ended up with a semicolon
	std::cout << "a is " << a << std::endl; // since a is an integer, the number behind the decimal will be truncated

	float b = a;   // here we cast a (integer) to b (float) (both are numeric, so it is fine)
	b = b + 3.5;
	std::cout << "b is " << b << std::endl; 

	double f = 100.0;
	double c = f_to_celsius(f);
	double k = f_to_Kelvin(f);
	std::cout << "F = " << f << ", C = " << c << std::endl;
	std::cout << "F = " << f << ", K = " << k << std::endl;

	count(5);

	std::vector<double> my_vector;
	my_vector.push_back(3.1415);
	std::cout << "0th element is " << my_vector[0] << std::endl;
	std::cout << "0th element is " << my_vector.at(0) << std::endl;

	std::cout << "1st element is " << my_vector[1] << std::endl;
	//std::cout << "1st element is " << my_vector.at(1) << std::endl;

	std::cout << "My vector has " << my_vector.size() << " elements" << std::endl;

	std::vector<double> pi_vector;

	for(int i=1; i <=5; i++)
		pi_vector.push_back(3.1415 * i);
	std::cout << "2nd element of pi_vector: " << pi_vector[1] << std::endl; 

	print_vector_1(pi_vector);
	std::cout << "\n" << std::endl;
	print_vector_2(pi_vector);

	std::string s = "This is a string.";
	std::cout << s << std::endl;
	
	Eigen::MatrixXd  mat(2, 3); // X: the size is not decided before compiling, d: double precision
	mat(0,0) = 1.0;
	mat(0,1) = 2.0;
	mat(0,2) = 3.0;
	mat(1,0) = 4.0;
	mat(1,1) = 5.0;
	mat(1,2) = 6.0; 
	std::cout << "The matrix 'mat' is "<< mat << std::endl; // Note that this is not doble in std vector (<vector>)
	
	Eigen::MatrixXd mat2 = mat * mat.transpose();
	std::cout << "Matrix mutiplication: \n";
	std::cout << mat2 << std::endl;

	Eigen::VectorXd vec(3); 
	vec(0) = vec(1) = vec(2) = 1.0; // All of the elements in the vector are 1.
	std::cout << "The vector 'vec' is " << vec << std::endl;
	std::cout << "v.v= " << vec.dot(vec) << std::endl;  // dot product

	// 2x3 * 3x1 = 2x1
	Eigen::MatrixXd vmult = mat * vec;
	std::cout << "vmult: " << vmult << std::endl;
	std::cout << "rows: " << vmult.rows() << std::endl;
	std::cout << "columns: " << vmult.cols() << std::endl;

	return 0;   // We must return something!
}