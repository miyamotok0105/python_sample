#include <cv.h>
#include <highgui.h>
#include <math.h>

//g++ `pkg-config --libs opencv pkg-config --cflags opencv` capture_fromfile.c -o capture_fromfile

int main(int argc, char* argv[])
{
    cvInitSystem(argc, argv);
    cvNamedWindow("video frames");
     
    //動画ファイルを開く
    CvCapture* capture = cvCaptureFromFile(argv[1]);
     
    //フレームレートを取得
    double fps = cvGetCaptureProperty(capture, CV_CAP_PROP_FPS);
     
    IplImage* captured_frame = 0;
    while((captured_frame = cvQueryFrame(capture)) != 0) {
        cvShowImage("video frames", captured_frame);
         
        //4倍速で再生するための時間待ち。
        int ch = cvWaitKey ( 1000.0 / (4 * fps) );
        if (ch == '\x1b') {
            // ESC キー
            break;
        }
    }
    cvDestroyAllWindows();
    cvReleaseCapture(&capture);
}

