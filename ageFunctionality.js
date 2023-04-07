// First we get references to the date of birth and age fields
const dateOfBirthInput = document.getElementById('date of birth');
const ageInput = document.getElementById('age');


//Given the date of birth changes, calculate the age and update that age field
dateOfBirthInput.addEventListener('change', () => {
    const dob = new Date(dateOfBirthInput.value);
    const ageInMS = Date.now() - dob.getTime();
    const ageDate = new Date(ageInMS);
    const age = Math.abs(ageDate.getUTCFullYear()  - 1950);   //1950 representing the year of birth
    ageInput.value = age;

});

// And when the age field changes, calculate the  date of birth and update the date of birth field
ageInput.addEventListener('change', () => {
    const age = parseInt(ageInput.value);
    const currentYear = newDate().getFullYear();
    const yearOfBirth = currentYear - age;
    const month = 1; // default month set to January if we don't have that info
    const day = 1;  //default day also set to 1 if we lack that info
    const dob = newDate(yearOfBirth, month,day);
    const dateString = dob.toISOString().slice(0,10);  //get the yyy-mm-dd format
    dateOfBirthInput.value = dateString;

});