#include <cv.h>
#include <highgui.h>
#include <math.h>
//005:回転移動のためのピクセルサンプリング cvGetQuadrangleSubPix
//g++ `pkg-config --cflags opencv` `pkg-config --libs opencv` 005.cpp -o 005

int
main (int argc, char **argv)
{
  int angle = 45;
  float m[6];
  IplImage *src_img = 0, *dst_img = 0;
  CvMat M;

  // (1)画像の読み込み，出力用画像領域の確保を行なう
  if (argc >= 2)
    src_img = cvLoadImage (argv[1], CV_LOAD_IMAGE_ANYDEPTH | CV_LOAD_IMAGE_ANYCOLOR);
  if (src_img == 0)
    return -1;
  dst_img = cvCloneImage (src_img);

  // (2)回転のための行列（アフィン行列）要素を設定し，CvMat行列Mを初期化する
  m[0] = (float) (cos (angle * CV_PI / 180.));
  m[1] = (float) (-sin (angle * CV_PI / 180.));
  m[2] = src_img->width * 0.5;
  m[3] = -m[1];
  m[4] = m[0];
  m[5] = src_img->height * 0.5;
  cvInitMatHeader (&M, 2, 3, CV_32FC1, m, CV_AUTOSTEP);

  // (3)指定された回転行列により，GetQuadrangleSubPixを用いて画像全体を回転させる
  cvGetQuadrangleSubPix (src_img, dst_img, &M);

  // (4)結果を表示する
  cvNamedWindow ("src", CV_WINDOW_AUTOSIZE);
  cvNamedWindow ("dst", CV_WINDOW_AUTOSIZE);
  cvShowImage ("src", src_img);
  cvShowImage ("dst", dst_img);
  cvWaitKey (0);

  cvDestroyWindow ("src");
  cvDestroyWindow ("dst");
  cvReleaseImage (&src_img);
  cvReleaseImage (&dst_img);

  return 1;
}
