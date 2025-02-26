// Функция для применения маски
function applyPhoneMask(input) {
    input.addEventListener('input', function (e) {
        let value = e.target.value.replace(/\D/g, ''); // Удаляем все нецифровые символы
        let formattedValue = '';

        if (value.length > 0) {
            formattedValue = '+7 '; // Добавляем код страны
        }
        if (value.length > 1) {
            formattedValue += '(' + value.substring(1, 4); // Добавляем первые три цифры
        }
        if (value.length > 4) {
            formattedValue += ') ' + value.substring(4, 7); // Добавляем следующие три цифры
        }
        if (value.length > 7) {
            formattedValue += '-' + value.substring(7, 9); // Добавляем следующие две цифры
        }
        if (value.length > 9) {
            formattedValue += '-' + value.substring(9, 11); // Добавляем последние две цифры
        }

        e.target.value = formattedValue; // Устанавливаем отформатированное значение
    });
}

// Применяем маску к полю ввода
// const phoneInput = document.getElementById('id_phone1');
const phoneInput = document.getElementsByClassName('form-phone-input');
applyPhoneMask(phoneInput[0]);