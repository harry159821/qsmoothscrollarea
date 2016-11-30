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
	scrollArea->setSmoothMode(QSmoothScrollArea::LINEAR);
    scrollArea->setWidget(imageLabel);
	scrollArea->setDuration(400);
	
    QGridLayout *layout = new QGridLayout(win);
	layout->addWidget(scrollArea);
	layout->setContentsMargins(1,1,1,1);
	win->setLayout(layout);

    win->show();
	win->resize(500,500);

    return app.exec();
}