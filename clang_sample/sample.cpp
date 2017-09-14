#include <opencv2/highgui/highgui.hpp>
//g++ `pkg-config --libs opencv pkg-config --cflags opencv` sample.cpp -o samplecpp
int main()
{
	cv::Mat img = cv::imread("./img1.jpg", CV_LOAD_IMAGE_COLOR);
	cv::imshow("opencvtest", img);
	cv::waitKey(0);
	return 0;
}

