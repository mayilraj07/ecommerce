
  $(document).ready(function(){
    $('.alert').fadeOut(4000)

    $('.plus-btn').click(function(){
      var pid = $(this).attr('pid').toString()
      console.log(pid)
      var qty = this.parentNode.children[2]
      console.log(qty)
      $.ajax({
        type:'GET',
        url:'/pluscart',
        data:{
          product_id: pid
        },
        success:function(data){
          console.log('data = ',data)
          qty.innerText = data.quantity
          document.getElementById('amount').innerHTML = `&#8377 ${data.amount}`
          document.getElementById('totalamount').innerHTML = `&#8377 ${data.totalamount}`
          delivery_cost = document.getElementById('delivery-cost')
          if(data.amount >= data.min_amount){
            delivery_cost.innerText = 'Free'
            delivery_cost.classList.add('text-success')
          }
           
        }
      })
    })

    $('.minus-btn').click(function(){
      var id = $(this).attr('pid').toString()
      var qty = this.parentNode.children[2]
      $.ajax({
        type:'GET',
        url:'/minusCart',
        data:{
          product_id: id
        },
        success:function(data){
          console.log('data = ',data)
          qty.innerText = data.quantity
          document.getElementById('amount').innerHTML = `&#8377 ${data.amount}`
          document.getElementById('totalamount').innerHTML = `&#8377 ${data.totalamount}` 
          delivery_cost = document.getElementById('delivery-cost')
          if(data.amount < data.min_amount){
            delivery_cost.innerHTML = `&#8377 ${40}`
            delivery_cost.classList.remove('text-success')
          }  
        }
      })
    })

    $('.increment').click(function(){
      var pid = $(this).attr('pid').toString()
      console.log(pid)
      var qty = this.parentNode.children[2]
      console.log(qty)
      $.ajax({
        type:'GET',
        url:'/addCount',
        data:{
          product_id: pid
        },
        success:function(data){
          console.log('data = ',data)
          qty.innerText = data.quantity
          document.getElementById('amount').innerHTML = `&#8377 ${data.amount}`
          document.getElementById('totalamount').innerHTML = `&#8377 ${data.totalamount}`
          delivery_cost = document.getElementById('delivery-cost')
          if(data.amount >= data.min_amount){
            delivery_cost.innerText = 'Free'
            delivery_cost.classList.add('text-success')
          }
           
        }
      })
    })

    $('.decrement').click(function(){
      var id = $(this).attr('pid').toString()
      var qty = this.parentNode.children[2]
      $.ajax({
        type:'GET',
        url:'/minusCount',
        data:{
          product_id: id
        },
        success:function(data){
          console.log('data = ',data)
          qty.innerText = data.quantity
          document.getElementById('amount').innerHTML = `&#8377 ${data.amount}`
          document.getElementById('totalamount').innerHTML = `&#8377 ${data.totalamount}`
          delivery_cost = document.getElementById('delivery-cost')
          if(data.amount < data.min_amount){
            delivery_cost.innerHTML = `&#8377 ${40}`
            delivery_cost.classList.remove('text-success')
          }   
        }
      })
    })

    $('.plus-qty').click(function(){
      var pid = $(this).attr('pid').toString()
      console.log(pid)
      var qty = this.parentNode.children[2]
      console.log(qty)
      $.ajax({
        type:'GET',
        url:'/addQty',
        data:{
          product_id: pid
        },
        success:function(data){
          console.log('data = ',data)
          qty.innerText = data.quantity
          document.getElementById('amount').innerHTML = `&#8377 ${data.amount}`
          document.getElementById('totalamount').innerHTML = `&#8377 ${data.totalamount}`
          delivery_cost = document.getElementById('delivery-cost')
          if(data.amount >= data.min_amount){
            delivery_cost.innerText = 'Free'
            delivery_cost.classList.add('text-success')
          }
          
        }
      })
    })

    $('.minus-qty').click(function(){
      var id = $(this).attr('pid').toString()
      var qty = this.parentNode.children[2]
      $.ajax({
        type:'GET',
        url:'/minQty',
        data:{
          product_id: id
        },
        success:function(data){
          console.log('data = ',data)
          qty.innerText = data.quantity
          document.getElementById('amount').innerHTML = `&#8377 ${data.amount}`
          document.getElementById('totalamount').innerHTML = `&#8377 ${data.totalamount}`
          delivery_cost = document.getElementById('delivery-cost')
          if(data.amount < data.min_amount){
            delivery_cost.innerHTML = `&#8377 ${40}`
            delivery_cost.classList.remove('text-success')
          }
        }
      })
    })

  })

  