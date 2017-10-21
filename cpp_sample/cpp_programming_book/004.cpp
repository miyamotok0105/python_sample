#include <cv.h>
#include <highgui.h>
//004:並進移動のためのピクセルサンプリング cvGetRectSubPix
//g++ `pkg-config --cflags opencv` `pkg-config --libs opencv` 004.cpp -o 004

int
main (int argc, char **argv)
{
  IplImage *src_img = 0, *dst_img = 0;
  CvPoint2D32f center;

  // (1)画像の読み込み，出力用画像領域の確保を行なう
  if (argc >= 2)
    src_img = cvLoadImage (argv[1], CV_LOAD_IMAGE_ANYDEPTH | CV_LOAD_IMAGE_ANYCOLOR);
  if (src_img == 0)
    return -1;
  dst_img = cvCloneImage (src_img);

  // (2)dst_imgの画像中心になるsrc_img中の位置centerを指定する
  center.x = src_img->width - 1;
  center.y = src_img->height - 1;

  // (3)centerが画像中心になるように，GetRectSubPixを用いて画像全体をシフトさせる
  cvGetRectSubPix (src_img, dst_img, center);


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
