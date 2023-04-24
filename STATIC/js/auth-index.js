const signinBtn = document.querySelector('#signin-btn');
        signinBtn.addEventListener('click', (event) => {
            event.preventDefault();
            const myProgress = document.getElementById("myProgress");
            myProgress.style.backgroundColor = "#ddd";
            let i = 0;
         
            if (i == 0) {
                i = 1;
                const elem = document.getElementById("myBar");
                let width = 5;
                const id = setInterval(frame, 30);
                
                function frame() {
                    if (width >= 100) {
                        clearInterval(id);
                        i = 0;
                    } else {
                        width++;
                        elem.style.width = width + "%";
                    }
                }
            }
    
            setTimeout(()=>{
                window.location.href = "../patients/index.html";
            },3000)
        });



        // showing or hidding the password functionality
        const showHidePassword = document.querySelector(".ti-eye");

        showHidePassword.addEventListener("click", (event)=>{

            event.preventDefault();
            let dataType = ("message")? "password ": "text"
           
            document.querySelector("#password").setAttribute("type","text")
            console.log("hello")

        })