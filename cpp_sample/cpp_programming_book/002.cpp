#include <cv.h>
#include <highgui.h>
#include <stdio.h>
#include <opencv2/opencv.hpp>
//002:エッジの検出 cvSobel, cvLaplace, cvCanny
//g++ `pkg-config --cflags opencv` `pkg-config --libs opencv` 002.cpp -o 002

using namespace cv;
int
main (int argc, char **argv)
{
  IplImage *src_img, *dst_img1, *dst_img2, *dst_img3;
  IplImage *tmp_img;

  // (1)画像の読み込み
  if (argc != 2 || (src_img = cvLoadImage (argv[1], CV_LOAD_IMAGE_GRAYSCALE)) == 0)
    return -1;

  tmp_img = cvCreateImage (cvGetSize (src_img), IPL_DEPTH_16S, 1);
  dst_img1 = cvCreateImage (cvGetSize (src_img), IPL_DEPTH_8U, 1);
  dst_img2 = cvCreateImage (cvGetSize (src_img), IPL_DEPTH_8U, 1);
  dst_img3 = cvCreateImage (cvGetSize (src_img), IPL_DEPTH_8U, 1);

  // (2)Sobelフィルタによる微分画像の作成
  cvSobel (src_img, tmp_img, 1, 0);
  cvConvertScaleAbs (tmp_img, dst_img1);

  // (3)画像のLaplacianの作成
  cvLaplace (src_img, tmp_img);
  cvConvertScaleAbs (tmp_img, dst_img2);

  // (4)Cannyによるエッジ画像の作成
  cvCanny (src_img, dst_img3, 50.0, 200.0);

  // (5)画像の表示
  cvNamedWindow ("Original", CV_WINDOW_AUTOSIZE);
  cvShowImage ("Original", src_img);
  cvNamedWindow ("Sobel", CV_WINDOW_AUTOSIZE);
  cvShowImage ("Sobel", dst_img1);
  cvNamedWindow ("Laplace", CV_WINDOW_AUTOSIZE);
  cvShowImage ("Laplace", dst_img2);
  cvNamedWindow ("Canny", CV_WINDOW_AUTOSIZE);
  cvShowImage ("Canny", dst_img3);
  cvWaitKey (0);

  cvDestroyWindow ("Original");
  cvDestroyWindow ("Sobel");
  cvDestroyWindow ("Laplace");
  cvDestroyWindow ("Canny");
  cvReleaseImage (&src_img);
  cvReleaseImage (&dst_img1);
  cvReleaseImage (&dst_img2);
  cvReleaseImage (&dst_img3);
  cvReleaseImage (&tmp_img);

  return 0;
}