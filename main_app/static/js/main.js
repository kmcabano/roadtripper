const picker = MCDatepicker.create({
  el: '#id_date',
  dateFormat: 'yyyy-mm-dd',
  closeOnBlur: true,
  selectedDate: new Date(),
})

const dateInput = document.getElementById('id_date')

dateInput.addEventListener("click", (evt) => {
  picker.open()
})