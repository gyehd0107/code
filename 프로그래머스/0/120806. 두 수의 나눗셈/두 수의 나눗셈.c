#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int num1, int num2) {
    double mean=0;
    mean= (double)num1/num2;
    
    int answer = mean*1000;
    return answer;
}