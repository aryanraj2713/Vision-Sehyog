import React from 'react'

function footer() {
    const vars = { 
        '--my-css-var': 10,
        '--my-another-css-var': "red" 
      }
  return (
    <div>
        <footer class="bg-light text-center text-lg-start">
            <div class="text-center p-3" style={{backgroundColor: "rgba(30,105,222,1)"}}>
                <a class="text-dark" href="">Made By team <strong>Vision-Sehyog</strong></a>  

            </div>
        </footer>


    </div>
  )
}

export default footer ;
