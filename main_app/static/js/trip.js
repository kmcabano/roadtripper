const startInput = document.getElementById('id_start')

const startPicker = MCDatepicker.create({
  el: '#id_start',
  dateFormat: 'yyyy-mm-dd',
  closeOnBlur: true,
  selectedDate: new Date(),
})

startInput.addEventListener("click", (evt) => {
  startPicker.open()
})

const endInput = document.getElementById('id_end')

const endPicker = MCDatepicker.create({
  el: '#id_end',
  dateFormat: 'yyyy-mm-dd',
  closeOnBlur: true,
  selectedDate: new Date(),
})

endInput.addEventListener("click", (evt) => {
  endPicker.open()
})