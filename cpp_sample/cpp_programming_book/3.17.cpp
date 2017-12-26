#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
//3.17 矩形領域のピクセル値をサブピクセル精度で取得する
//g++ `pkg-config --cflags opencv` `pkg-config --libs opencv` 3.17.cpp -o 3.17

int
main(int argc, char *argv[])
{
  cv::Mat src_img = cv::imread("../../img/hari.jpeg", 1);
  if(!src_img.data) return -1; 

  cv::Size patch_sie(100, 100);
  cv::Point2f center(250.0, 250.0);
  cv::Mat dst_img;
  // 矩形領域ピクセル値をサブピクセル精度で取得
  cv::getRectSubPix(src_img, patch_sie, center, dst_img);
  
  cv::namedWindow("image", CV_WINDOW_AUTOSIZE|CV_WINDOW_FREERATIO);
  cv::imshow("image", dst_img);
  cv::waitKey(0);
}
