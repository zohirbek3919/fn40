def sell(self, count):
    if count > 0 and count <= self.__miqdor:
        self.__miqdor -= count
    else:
        raise ValueError(f"Xatolik! {count} 0 dan katta va mavjud miqdordan oshmasligi kerak")
