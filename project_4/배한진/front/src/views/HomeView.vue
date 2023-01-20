<template>
  <div class="home">


  <br/>
  <div class="w-full md:w-96 md:max-w-full mx-auto">
  <div class="p-6 border border-gray-300 sm:rounded-md">
    <form
      @submit.prevent="sendPost"
    >
      <label class="block mb-6">
        <span class="text-gray-700">Predict All Class</span>
        <div class = 'm-auto text-center flex justify-center'>
        <input
          required
          name="photo"
          type="file"
          id = "file"
          class="
            inline-block
            text-center
            
            mt-1
            focus:border-indigo-300
            focus:ring
            focus:ring-indigo-200
            focus:ring-opacity-50
          "
        />
        </div>
      </label>
      <div class="mb-6">
        <button
          type="submit"
          class="
            h-10
            px-5
            text-indigo-100
            bg-indigo-700
            rounded-lg
            transition-colors
            duration-150
            focus:shadow-outline
            hover:bg-indigo-800
          
          "
        >
          Upload
        </button>
      </div>

    </form>
  </div>
</div>
<br/>
<div>
<ul style="list-style:none;">
        <li v-for="item in value">
            {{item}}

        </li>
    </ul>
  </div>
  <br/>
<hr>

<br/>
  <div class="w-full md:w-96 md:max-w-full mx-auto">
  <div class="p-6 border border-gray-300 sm:rounded-md">
    <form
      @submit.prevent="sendPost2"
    >
    <label class="block mb-6">
        <span class="text-gray-700">Predict Single Class</span>
        <div class = 'm-auto text-center flex justify-center'>
        <input
          required
          name="photo"
          type="file"
          id = "file2"
          class="
            inline-block
            text-center
            
            mt-1
            focus:border-indigo-300
            focus:ring
            focus:ring-indigo-200
            focus:ring-opacity-50
          "
        />
        </div>
      </label>
      <div class="mb-6">
    <input type="text" id="value_num" placeholder = "value_num" class=" text-center bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
</div>
      <div class="mb-6">
        <button
          type="submit"
          class="
            h-10
            px-5
            text-indigo-100
            bg-indigo-700
            rounded-lg
            transition-colors
            duration-150
            focus:shadow-outline
            hover:bg-indigo-800
          "
        >
          Upload
        </button>
      </div>

    </form>
  </div>
</div>
<br/>
<div>
<ul style="list-style:none;">
  <li v-for="item in value_single">
            {{item}}

        </li>
    </ul>
  </div>
  <br/>
<hr>

  </div>
</template>

<script>

import HelloWorld from '@/components/HelloWorld.vue'
import axios from 'axios';

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  },
  data(){
    return{
      value: [],
      value_single: []
    }
  },
  methods: {
    sendPost: function(){

      var url = 'http://localhost:8021/predict_all';
      const frm = new FormData()
      var image = document.getElementById("file");
      console.log(image);

      frm.append("image", image.files[0]);
      console.log(frm)
      
      axios.post(url, frm,  {headers: {
    'Content-Type': 'multipart/form-data'
     }})
      .then((Response) => {

        var data_in = Response.data
        for (var step = 1; step < 7; step++) {
        var value_ = 'value_'
        var value_in = data_in[value_ + step]
        this.value.push(value_in)
      }
      })
      .catch((error) => {
        console.log(error)
      })

    
  },
  sendPost2: function(){

var url = 'http://localhost:8021/predict';
const frm = new FormData()
var image = document.getElementById("file2");
console.log(image);
var value_num = document.getElementById("value_num");
frm.append("image", image.files[0]);
console.log(frm)
frm.append("value_num", value_num.value);
axios.post(url, frm,  {headers: {
'Content-Type': 'multipart/form-data'
}})
.then((Response) => {

  var data_in = Response.data
  this.value_single.push(data_in)
//   for (var step = 1; step < 7; step++) {
//   var value_ = 'value_'
//   var value_in = data_in[value_ + step]
//   this.value.push(value_in)
// }
})
.catch((error) => {
  console.log(error)
})


}
}

}
</script>
