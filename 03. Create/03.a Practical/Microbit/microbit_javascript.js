/**
 * buffer for serial output
 */
input.onButtonPressed(Button.A, function () {
    started = !(started)
})
// no music under low risk
function evaluate (score: number) {
    if (started) {
        basic.showNumber(score)
        // high risk
        // middle risk
        if (score > 5) {
            music.ringTone(440)
        } else if (score > 2) {
            music.ringTone(262)
        } else {
            music.stopAllSounds()
        }
    } else {
        basic.clearScreen()
    }
}
function readHumidity () {
    dht11_dht22.queryData(
    DHTtype.DHT11,
    DigitalPin.P0,
    true,
    false,
    false
    )
    if (dht11_dht22.readDataSuccessful()) {
        return dht11_dht22.readData(dataType.humidity)
    } else {
        return humidity
    }
}
function scoring (temp: number, rh: number, lighting: number) {
    score = 0
    // temperature
    if (temp >= 40) {
        // extreme condition
        score += 5
    } else if (temp >= 30) {
        score += 2
    } else if (temp >= 25) {
        score += 1
    }
    // humidity
    if (rh <= 30) {
        score += 2
    } else if (rh <= 35) {
        score += 1
    }
    // lighting
    // level about 200 in computer classroom
    // stronger light potentially means
    // higher temp. and dryer air
    if (lighting >= 210) {
        score += 1
    }
}
let serial_string = ""
let score = 0
let started = false
let humidity = 0
music.setVolume(10)
// reads kind of unreliably
// thus give a initial value
humidity = 36
serial.redirect(
SerialPin.USB_TX,
SerialPin.USB_RX,
BaudRate.BaudRate115200
)
serial.redirectToUSB()
basic.showString("W")
basic.forever(function () {
    if (started) {
        humidity = readHumidity()
        for (let index = 0; index < 3; index++) {
            scoring(input.temperature(), humidity, input.lightLevel())
            evaluate(score)
            basic.pause(1000)
        }
        serial_string = " " + input.temperature().toString() + " " + humidity.toString() + " " + input.lightLevel().toString() + " " + score
        serial.writeString(serial_string)
        serial.writeLine("")
    }
})
