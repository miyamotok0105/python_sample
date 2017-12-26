#include <stdio.h>
#include <opencv2/opencv.hpp>
//g++ `pkg-config --cflags opencv` `pkg-config --libs opencv` 001.cpp -o 001
using namespace cv;

int main(int argc, char** argv ) {
    Mat image;
    image = imread("../../img/hari.jpeg", 1 );
    if ( !image.data ) {
        printf("No image data \n");
        return -1;
    }
    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image", image);
    waitKey(0);
    return 0;
}