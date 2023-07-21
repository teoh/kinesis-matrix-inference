# I took this from qmk firmware for the kinesis advantage 2
KEY_LAYOUT = """
           KC_ESC, KC_F1  ,KC_F2  ,KC_F3  ,KC_F4  ,KC_F5  ,KC_F6  ,KC_F7  ,KC_F8,
           KC_EQL, KC_1   ,KC_2   ,KC_3   ,KC_4   ,KC_5   ,
           KC_TAB, KC_Q   ,KC_W   ,KC_E   ,KC_R   ,KC_T   ,
           KC_CAPS,KC_A   ,KC_S   ,KC_D   ,KC_F   ,KC_G   ,
           KC_LSFT,KC_Z   ,KC_X   ,KC_C   ,KC_V   ,KC_B   ,
                   KC_GRV ,KC_INS ,KC_LEFT,KC_RGHT,
			   KC_LCTL,KC_LALT,
                                    KC_HOME,
                           KC_BSPC,KC_DEL ,KC_END ,
    KC_F9  ,KC_F10 ,KC_F11 ,KC_F12 ,KC_PSCR ,KC_SCRL  ,KC_PAUS, KC_NO, QK_BOOT,
	KC_6   ,KC_7   ,KC_8   ,KC_9   ,KC_0   ,KC_MINS,
	KC_Y   ,KC_U   ,KC_I   ,KC_O   ,KC_P   ,KC_BSLS,
	KC_H   ,KC_J   ,KC_K   ,KC_L   ,KC_SCLN,KC_QUOT,
	KC_N   ,KC_M   ,KC_COMM,KC_DOT ,KC_SLSH,KC_RSFT,
		KC_UP  ,KC_DOWN,KC_LBRC,KC_RBRC,
           KC_RGUI,KC_RCTL,
           KC_PGUP,
           KC_PGDN,KC_ENTER ,KC_SPC
"""
IDENTIFIER_LAYOUT = """
    kC0, kD0, kE0, kC1, kD1, kE1, kC2, kD2, kE2,  \
    k00, k10, k20, k30, k40, k50,                 \
    k01, k11, k21, k31, k41, k51,                 \
    k02, k12, k22, k32, k42, k52,                 \
    k03, k13, k23, k33, k43, k53,                 \
         k14, k24, k34, k54,                      \
                             k56, k55,            \
                                  k35,            \
                        k36, k46, k25,            \
                                                  \
    kC3, kD3, kE3, kC4, kD4, kE4, kC5, kE5, kD5,  \
                   k60, k70, k80, k90, kA0, kB0,  \
                   k61, k71, k81, k91, kA1, kB1,  \
                   k62, k72, k82, k92, kA2, kB2,  \
                   k63, k73, k83, k93, kA3, kB3,  \
                        k64, k84, k94, kA4,       \
              k96, k85,                           \
              k86,                                \
              k66, k75, k65                       \
"""
IDENTIFIER_MATRIX = """
    { k00,  k01,  k02,  k03,  ___,  ___,  ___ },
    { k10,  k11,  k12,  k13,  k14,  ___,  ___ },
    { k20,  k21,  k22,  k23,  k24,  k25,  ___ },
    { k30,  k31,  k32,  k33,  k34,  k35,  k36 },
    { k40,  k41,  k42,  k43,  ___,  ___,  k46 },
    { k50,  k51,  k52,  k53,  k54,  k55,  k56 },
    { k60,  k61,  k62,  k63,  k64,  k65,  k66 },
    { k70,  k71,  k72,  k73,  ___,  k75,  ___ },
    { k80,  k81,  k82,  k83,  k84,  k85,  k86 },
    { k90,  k91,  k92,  k93,  k94,  ___,  k96 },
    { kA0,  kA1,  kA2,  kA3,  kA4,  ___,  ___ },
    { kB0,  kB1,  kB2,  kB3,  ___,  ___,  ___ },
    { kC0,  kC1,  kC2,  kC3,  kC4,  kC5,  ___ },
    { kD0,  kD1,  kD2,  kD3,  kD4,  kD5,  ___ },
    { kE0,  kE1,  kE2,  kE3,  kE4,  kE5,  ___ },
"""
NUM_COLS = 7
ROW_TO_NAME = """
        LINE_PIN8,      /* ROW_EQL */
            LINE_PIN9,  /* ROW_1 */
            LINE_PIN10, /* ROW_2 */
            LINE_PIN11, /* ROW_3 */
            LINE_PIN7,  /* ROW_4 */
            LINE_PIN16, /* ROW_5 */
            LINE_PIN5,  /* ROW_6 */
            LINE_PIN3,  /* ROW_7 */
            LINE_PIN4,  /* ROW_8 */
            LINE_PIN1,  /* ROW_9 */
            LINE_PIN0,  /* ROW_0 */
            LINE_PIN2,  /* ROW_MIN */
            LINE_PIN17, /* ROW_ESC */
            LINE_PIN23, /* ROW_F1 */
            LINE_PIN21 /* ROW_F2 */
"""
COL_TO_NAME = """
        LINE_PIN18,     /* COL_0 */
            LINE_PIN14, /* COL_1 */
            LINE_PIN15, /* COL_2 */
            LINE_PIN20, /* COL_3 */
            LINE_PIN22, /* COL_4 */
            LINE_PIN19, /* COL_5 */
            LINE_PIN6   /* COL_6 */
"""

# i had to do this manually
# based on this diagram: https://github.com/kinx-project/kint/blob/main/schematic-v2021-06-26.pdf
CLUSTER_PINS = {
    "LEFT_13_LT": [
        "COL_0",
        "ROW_5",
        "ROW_4",
        "ROW_3",
        "",
        "ROW_2",
        "ROW_1",
        "ROW_EQL",
        "COL_1",
        "",
        "COL_2",
        "COL_3",
        "COL_4",
    ],
    "TOP_LEFT": [
        "COL_2",
        "ROW_ESC",
        "ROW_F1",
        "ROW_F2",
        "COL_1",
        "ROW_F1",
        "ROW_F2",
        "COL_0",
        "",
        "ROW_F1",
        "ROW_F2",
        "",
        "",
    ],
    "THUMB_LEFT_BAK_KB600": [
        "",
        "",
        "",
        "",
        "",
        "ROW_2",
        "",
        "",
        "COL_5",
        "COL_6",
        "ROW_3",
        "ROW_4",
        "ROW_5",
    ],
    "RIGHT_13_DOWN": [
        "ROW_6",
        "ROW_8",
        "ROW_7",
        "COL_4",
        "",
        "ROW_MIN",
        "COL_3",
        "COL_2",
        "COL_1",
        "COL_0",
        "",
        "ROW_9",
        "ROW_0",
    ],
    "TOP_RIGHT": [
        "",
        "",
        "ROW_F1",
        "ROW_F2",
        "COL_4",
        "ROW_F1",
        "ROW_F2",
        "COL_3",
        "ROW_ESC",
        "COL_5",
        "COL_5",
        "ROW_F2",
        "ROW_F1",
    ],
    "THUMB_RIGHT_SPC_KB600": [
        "",
        "",
        "ROW_9",
        "ROW_7",
        "ROW_8",
        "ROW_6",
        "COL_6",
        "COL_5",
        "",
        "",
        "",
        "",
        "",
    ],
}

# i also had to do this manually
CLUSTER_KEYS = {
    "LEFT_13_LT": [
        key.strip()
        for key in """
           KC_EQL, KC_1   ,KC_2   ,KC_3   ,KC_4   ,KC_5   ,
           KC_TAB, KC_Q   ,KC_W   ,KC_E   ,KC_R   ,KC_T   ,
           KC_CAPS,KC_A   ,KC_S   ,KC_D   ,KC_F   ,KC_G   ,
           KC_LSFT,KC_Z   ,KC_X   ,KC_C   ,KC_V   ,KC_B   ,
                   KC_GRV ,KC_INS ,KC_LEFT,KC_RGHT,
    """.split(
            ","
        )
        if key.strip()
    ],
    "TOP_LEFT": [
        key.strip()
        for key in """
    KC_ESC, KC_F1  ,KC_F2  ,KC_F3  ,KC_F4  ,KC_F5  ,KC_F6  ,KC_F7  ,KC_F8,
    """.split(
            ","
        )
        if key.strip()
    ],
    "THUMB_LEFT_BAK_KB600": [
        key.strip()
        for key in """
    			   KC_LCTL,KC_LALT,
                                    KC_HOME,
                           KC_BSPC,KC_DEL ,KC_END ,
    """.split(
            ","
        )
        if key.strip()
    ],
    "RIGHT_13_DOWN": [
        key.strip()
        for key in """
    	KC_6   ,KC_7   ,KC_8   ,KC_9   ,KC_0   ,KC_MINS,
	KC_Y   ,KC_U   ,KC_I   ,KC_O   ,KC_P   ,KC_BSLS,
	KC_H   ,KC_J   ,KC_K   ,KC_L   ,KC_SCLN,KC_QUOT,
	KC_N   ,KC_M   ,KC_COMM,KC_DOT ,KC_SLSH,KC_RSFT,
		KC_UP  ,KC_DOWN,KC_LBRC,KC_RBRC,
    """.split(
            ","
        )
        if key.strip()
    ],
    "TOP_RIGHT": [
        key.strip()
        for key in """
    KC_F9  ,KC_F10 ,KC_F11 ,KC_F12 ,KC_PSCR ,KC_SCRL  ,KC_PAUS, KC_NO, QK_BOOT,
    """.split(
            ","
        )
        if key.strip()
    ],
    "THUMB_RIGHT_SPC_KB600": [
        key.strip()
        for key in """
               KC_RGUI,KC_RCTL,
           KC_PGUP,
           KC_PGDN,KC_ENTER ,KC_SPC
    """.split(
            ","
        )
        if key.strip()
    ],
}

# Elite-C row pins
ELITE_C_ROW_PINS = [
    pin.strip()
    for pin in "B3, B1, F7, F6, F5, F4, D3, D2, D1, D0, D4, C6, D7, E6, B4".split(",")
]

# Elite-C col pins
ELITE_C_COL_PINS = [pin.strip() for pin in "B2, B6, B7, D5, C7, F1, F0".split(",")]
