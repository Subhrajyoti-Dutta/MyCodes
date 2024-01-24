#include <iostream>
#include <array>

void printarr(int arr[], int length) {
	for (int i = 0; i < length; i++) {
		std::cout << arr[i] << " ";
	}
	std::cout << "\n";
}

int SortedListInsert(int arr[]) {
	int newList[] = { arr[0] };
	bool inserted = false;
	return 0;
}

int* InsertionSort(int arr[],int leng_arr) {
	for (int i = 1; i < leng_arr; i++) {
		int key = arr[i];
		int j = i - 1;
		while (j >= 0 && arr[j] > key) {
			arr[j + 1] = arr[j];
			j--;
		}
		arr[j + 1] = key;
	}
	return arr;
}

int main() {
	int a[] = { 110,92,93,94 };
	int leng_a = sizeof(a) / sizeof(a[0]);
	int* arr1 = InsertionSort(a, leng_a);
	printarr(arr1,leng_a);
	return 0;
}