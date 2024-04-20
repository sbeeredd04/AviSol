#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu1;
MPU6050 mpu2;

Vector3D velocity1 = {0, 0, 0};
Vector3D velocity2 = {0, 0, 0};

unsigned long previousTime = 0;

void setup() {
    Serial.begin(9600);
    
    Wire.begin();
    
    mpu1.initialize();
    mpu2.initialize();
}

void loop() {
    unsigned long currentTime = millis();
    float deltaTime = (currentTime - previousTime) / 1000.0; // Convert to seconds

    Vector3D accel1 = mpu1.getAcceleration();
    Vector3D accel2 = mpu2.getAcceleration();
    
    // Calculate velocity by integrating acceleration
    velocity1.x += accel1.x * deltaTime;
    velocity1.y += accel1.y * deltaTime;
    velocity1.z += accel1.z * deltaTime;

    velocity2.x += accel2.x * deltaTime;
    velocity2.y += accel2.y * deltaTime;
    velocity2.z += accel2.z * deltaTime;

    float distance = sqrt(pow(accel2.x - accel1.x, 2) + pow(accel2.y - accel1.y, 2) + pow(accel2.z - accel1.z, 2));
    
    if (distance <= 5) {
        Serial.println("Descend to the ground or change elevation!");
    }

    // Print velocities
    Serial.print("Velocity1: ");
    Serial.print(velocity1.x);
    Serial.print(", ");
    Serial.print(velocity1.y);
    Serial.print(", ");
    Serial.println(velocity1.z);

    Serial.print("Velocity2: ");
    Serial.print(velocity2.x);
    Serial.print(", ");
    Serial.print(velocity2.y);
    Serial.print(", ");
    Serial.println(velocity2.z);

    previousTime = currentTime;
    
    delay(1000);
}