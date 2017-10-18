#include <boost/python.hpp>

int add(int lhs, int rhs)
{
    return lhs + rhs;
}

BOOST_PYTHON_MODULE(simple)
{
    using namespace boost::python;
    def("add", &add);
}