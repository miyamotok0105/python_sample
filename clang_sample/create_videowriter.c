#include <cv.h>
#include <highgui.h>
#include <math.h>
#include <highgui.h>
#include <iostream>

//g++ `pkg-config --libs opencv pkg-config --cflags opencv` create_videowriter.c -o create_videowriter

int main(int argc, char* argv[])
{
    IplImage *frame = NULL;

    //カメラの初期化（カメラの選択）
    CvCapture *capture = cvCaptureFromCAM(0);

    //画像サイズ
    int Width  = 640;
    int Height = 480;

    //取込サイズの設定
    cvSetCaptureProperty(capture, CV_CAP_PROP_FRAME_WIDTH,  Width);
    cvSetCaptureProperty(capture, CV_CAP_PROP_FRAME_HEIGHT, Height);

    //ウィンドウの表示
    cvNamedWindow ("Capture", CV_WINDOW_AUTOSIZE);

    //aviファイル設定
    double fps = 5.0;
    // CvVideoWriter* VideoWriter = cvCreateVideoWriter("avifile.avi", -1, fps, cvSize(Width, Height), 1 );
    CvVideoWriter* VideoWriter = cvCreateVideoWriter("sample.avi", -1, fps, cvSize(Width, Height), 1 );

    while (1) {
         //フレーム画像の取込
         frame = cvQueryFrame (capture);

         //１画面分の書込
         cvWriteFrame(VideoWriter, frame); 
                   
         //画像の表示
         cvShowImage ("Capture", frame);
                   
         //キー入力待ち（Escキーで終了）
         if (cvWaitKey (1000.0 / fps) == '\x1b')
              break;
    }

    //解放
    cvReleaseCapture (&capture);
    cvDestroyWindow ("Capture");
    cvReleaseVideoWriter(&VideoWriter);
}


