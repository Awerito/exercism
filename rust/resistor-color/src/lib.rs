use enum_iterator::IntoEnumIterator;
use int_enum::IntEnum;

#[repr(usize)]
#[derive(Clone, Copy, Debug, Eq, PartialEq, IntEnum, IntoEnumIterator)]
pub enum ResistorColor {
    Black = 0,
    Brown = 1,
    Red = 2,
    Orange = 3,
    Yellow = 4,
    Green = 5,
    Blue = 6,
    Violet = 7,
    Grey = 8,
    White = 9,
}

pub fn color_to_value(_color: ResistorColor) -> usize {
    _color as usize
}

pub fn value_to_color_string(value: usize) -> String {
    match ResistorColor::from_int(value) {
        Ok(resistor) => format!("{:?}", resistor),
        Err(_) => String::from("value out of range"),
    }
}

pub fn colors() -> Vec<ResistorColor> {
    Vec::from_iter(ResistorColor::into_enum_iter())
}
