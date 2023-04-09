class HealthMonitor:
    def __init__(self, name, age, heart_rate, blood_pressure, temperature):
        self.name = name
        self.age = age
        self.heart_rate = heart_rate
        self.blood_pressure = blood_pressure
        self.temperature = temperature

    def check_heart_rate(self):
        if self.heart_rate < 60 or self.heart_rate > 100:
            print("Warning: Abnormal heart rate detected!")
            return False
        else:
            print("Heart rate is within normal range.")
            return True

    def check_blood_pressure(self):
        if self.blood_pressure[0] < 90 or self.blood_pressure[1] > 120:
            print("Warning: Abnormal blood pressure detected!")
            return False
        else:
            print("Blood pressure is within normal range.")
            return True

    def check_temperature(self):
        if self.temperature < 97.0 or self.temperature > 99.0:
            print("Warning: Abnormal body temperature detected!")
            return False
        else:
            print("Body temperature is within normal range.")
            return True

    def run_health_checks(self):
        heart_rate_status = self.check_heart_rate()
        blood_pressure_status = self.check_blood_pressure()
        temperature_status = self.check_temperature()

        if heart_rate_status and blood_pressure_status and temperature_status:
            print("Overall health status: Normal")
        else:
            print("Overall health status: Abnormal")


# Example usage of the HealthMonitor class
patient1 = HealthMonitor("John", 30, 80, (110, 70), 98.6)
patient1.run_health_checks()
