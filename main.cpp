#include "qsmoothscrollarea.h"
#include <QtGui>
#include <QWidget>
#include <QGridLayout>
#include <QLabel>
#include <QImage>
#include <QPixmap>

int main(int argc, char * argv[])
{
    QApplication app(argc, argv);

    QWidget *win = new QWidget;

    QLabel *imageLabel = new QLabel(win);
    QImage image("test.png");
    imageLabel->setPixmap(QPixmap::fromImage(image));

    QSmoothScrollArea *scrollArea = new QSmoothScrollArea(win);
	scrollArea->setSmoothMode(QSmoothScrollArea::POW);
    scrollArea->setWidget(imageLabel);
	scrollArea->setDuration(300);
	
    QGridLayout *layout = new QGridLayout(win);
	layout->addWidget(scrollArea);
	layout->setContentsMargins(1,1,1,1);
	win->setLayout(layout);

    win->show();
	win->resize(247,480);

    return app.exec();
}