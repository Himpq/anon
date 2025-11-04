#include <Arduino.h>
#include <U8g2lib.h>
#include "anon.hpp"

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

// 替换为连接的针脚接口
#define OLED_MOSI 23
#define OLED_CLK  18
#define OLED_DC   27
#define OLED_CS   5
#define OLED_RESET 14

// SSD1315 128x64 SPI
U8G2_SSD1315_128X64_NONAME_F_4W_HW_SPI u8g2(
    U8G2_R0,
    /* cs=*/ 5,
    /* dc=*/ 27,
    /* reset=*/ 14
);

void setup() {
    u8g2.begin();
    u8g2.clearBuffer();
}

void drawBMP (uint8_t* bitmap) {
    u8g2.clearBuffer();
    u8g2.drawXBMP(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, bitmap);
    u8g2.sendBuffer();
}

void loop() {
    drawBMP((uint8_t*)anon1);
    delay(150);
    drawBMP((uint8_t*)anon2);
    delay(150);
}
