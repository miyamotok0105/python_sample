#include <boost/python.hpp>
 
 
char const* hello(){
  return "hello, world";
}
 
 
BOOST_PYTHON_MODULE( simple2 ){
   
  boost::python::def( "hello", hello );
 
}
