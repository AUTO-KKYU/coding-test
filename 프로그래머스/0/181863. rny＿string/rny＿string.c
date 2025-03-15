#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* rny_string) {
    int length = strlen(rny_string);
    int new_length = 0;

    // 'm'을 'rn'으로 바꿀 경우 증가할 길이 계산
    for (int i = 0; i < length; i++) {
        if (rny_string[i] == 'm')
            new_length += 2;  // 'm' → 'rn' (2글자)
        else
            new_length += 1;
    }

    // 새로운 문자열을 저장할 공간 동적 할당
    char* answer = (char*)malloc(new_length + 1); // +1 for null terminator
    if (answer == NULL) return NULL; // 메모리 할당 실패 시 예외 처리

    int j = 0;
    for (int i = 0; i < length; i++) {
        if (rny_string[i] == 'm') {
            answer[j++] = 'r';
            answer[j++] = 'n';
        } else {
            answer[j++] = rny_string[i];
        }
    }

    answer[j] = '\0';  // 문자열 종료 문자 추가
    return answer;
}