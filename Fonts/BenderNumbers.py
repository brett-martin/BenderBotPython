class BenderNumbers():

    _blank = [
	[0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]]

    _zero = [
	[0,0,0,0,0,0,0,0],
	[0,0,1,1,1,0,0,0],
	[0,1,0,0,0,1,0,0],
	[1,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[0,1,0,0,0,1,0,0],
	[0,0,1,1,1,0,0,0],
	[0,0,0,0,0,0,0,0]]

    _one = [
	[0,0,0,0,0,0,0,0],
	[0,0,0,1,0,0,0,0],
	[0,0,1,1,0,0,0,0],
	[0,1,0,1,0,0,0,0],
	[0,0,0,1,0,0,0,0],
	[0,0,0,1,0,0,0,0],
	[0,0,0,1,0,0,0,0],
	[0,0,0,1,0,0,0,0],
	[0,0,0,1,0,0,0,0],
	[0,0,0,1,0,0,0,0],
	[0,0,0,1,0,0,0,0],
	[0,0,0,1,0,0,0,0],
	[0,0,0,1,0,0,0,0],
	[0,0,0,1,0,0,0,0],
	[0,1,1,1,1,1,0,0],
	[0,0,0,0,0,0,0,0]]

    _two = [
	[0,0,0,0,0,0,0,0],
	[0,0,1,1,1,0,0,0],
	[0,1,0,0,0,1,0,0],
	[1,0,0,0,0,0,1,0],
	[0,0,0,0,0,0,1,0],
	[0,0,0,0,0,0,1,0],
	[0,0,0,0,0,1,0,0],
	[0,0,0,0,1,0,0,0],
	[0,0,0,1,0,0,0,0],
	[0,0,1,0,0,0,0,0],
	[0,1,0,0,0,0,0,0],
	[1,0,0,0,0,0,0,0],
	[1,0,0,0,0,0,0,0],
	[1,0,0,0,0,0,0,0],
	[0,1,1,1,1,1,1,0],
	[0,0,0,0,0,0,0,0]]

    _three = [
	[0,0,0,0,0,0,0,0],
	[0,0,1,1,1,0,0,0],
	[0,1,0,0,0,1,0,0],
	[1,0,0,0,0,0,1,0],
	[0,0,0,0,0,0,1,0],
	[0,0,0,0,0,0,1,0],
	[0,0,0,0,0,1,0,0],
	[0,0,0,0,1,0,0,0],
	[0,0,0,0,0,1,0,0],
	[0,0,0,0,0,0,1,0],
	[0,0,0,0,0,0,1,0],
	[0,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[0,1,0,0,0,1,0,0],
	[0,0,1,1,1,0,0,0],
	[0,0,0,0,0,0,0,0]]

    _four = [
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,1,0,0,0],
	[0,0,0,1,0,0,0,0],
	[0,0,0,1,0,0,0,0],
	[0,0,1,0,0,0,0,0],
	[0,0,1,0,0,0,1,0],
	[0,1,0,0,0,0,1,0],
	[0,1,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[1,1,1,1,1,1,1,0],
	[0,0,0,0,0,0,1,0],
	[0,0,0,0,0,0,1,0],
	[0,0,0,0,0,0,1,0],
	[0,0,0,0,0,0,1,0],
	[0,0,0,0,0,0,1,0],
	[0,0,0,0,0,0,0,0]]

    _five = [
	[0,0,0,0,0,0,0,0],
	[1,1,1,1,1,1,1,0],
	[1,0,0,0,0,0,0,0],
	[1,0,0,0,0,0,0,0],
	[1,0,0,0,0,0,0,0],
	[1,0,0,0,0,0,0,0],
	[1,1,0,0,0,0,0,0],
	[0,0,1,1,1,0,0,0],
	[0,0,0,0,0,1,0,0],
	[0,0,0,0,0,0,1,0],
	[0,0,0,0,0,0,1,0],
	[0,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[0,1,0,0,0,1,0,0],
	[0,0,1,1,1,0,0,0],
	[0,0,0,0,0,0,0,0]]

    _six = [
	[0,0,0,0,0,0,0,0],
	[0,0,1,1,1,0,0,0],
	[0,1,0,0,0,1,0,0],
	[1,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,0,0],
	[1,0,0,0,0,0,0,0],
	[1,0,0,0,0,0,0,0],
	[1,0,1,1,1,0,0,0],
	[1,1,0,0,0,1,0,0],
	[1,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[0,1,0,0,0,1,0,0],
	[0,0,1,1,1,0,0,0],
	[0,0,0,0,0,0,0,0]]

    _seven = [
	[0,0,0,0,0,0,0,0],
	[1,1,1,1,1,1,1,0],
	[0,0,0,0,0,0,1,0],
	[0,0,0,0,0,1,0,0],
	[0,0,0,0,0,1,0,0],
	[0,0,0,0,1,0,0,0],
	[0,0,0,0,1,0,0,0],
	[0,0,0,1,0,0,0,0],
	[0,0,0,1,0,0,0,0],
	[0,0,1,0,0,0,0,0],
	[0,0,1,0,0,0,0,0],
	[0,1,0,0,0,0,0,0],
	[0,1,0,0,0,0,0,0],
	[1,0,0,0,0,0,0,0],
	[1,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0]]

    _eight = [
	[0,0,0,0,0,0,0,0],
	[0,0,1,1,1,0,0,0],
	[0,1,0,0,0,1,0,0],
	[1,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[0,1,0,0,0,1,0,0],
	[0,0,1,1,1,0,0,0],
	[0,1,0,0,0,1,0,0],
	[1,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[0,1,0,0,0,1,0,0],
	[0,0,1,1,1,0,0,0],
	[0,0,0,0,0,0,0,0]]

    _nine = [
	[0,0,0,0,0,0,0,0],
	[0,0,1,1,1,0,0,0],
	[0,1,0,0,0,1,0,0],
	[1,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[0,1,0,0,0,1,1,0],
	[0,0,1,1,1,0,1,0],
	[0,0,0,0,0,0,1,0],
	[0,0,0,0,0,0,1,0],
	[0,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,0],
	[0,1,0,0,0,1,0,0],
	[0,0,1,1,1,0,0,0],
	[0,0,0,0,0,0,0,0]]

    def getNumber(self, number):
        numbers = {
            0: self._zero,
            1: self._one,
            2: self._two,
            3: self._three,
            4: self._four,
            5: self._five,
            6: self._six,
            7: self._seven,
            8: self._eight,
            9: self._nine
        }
        return numbers.get(number, self._blank)