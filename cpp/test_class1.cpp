#include <iostream>

class Player {
public:
	int x;
	int y;

	Player(int inix = 0, int iniy = 0) {
		x = inix;
		y = iniy;
	}

	void move(int xa, int ya) {
		x += xa;
		y += ya;
	}
};

int main()
{
	Player virat(0, 0);
	virat.move(1, 2);
	printf("%d\t",virat.x);
	printf("%d",virat.y);
	return 0;
}