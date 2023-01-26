<template>
  <div class="home flex mx-auto w-2/3 h-screen flex-row justify-evenly items-center">

    <div class=" w-auto md:w-96 md:max-w-full mx-auto">
      <div class="p-6 border  border-gray-300 sm:rounded-md">
        <form @submit.prevent="sendPost">
          <div class="flex justify-between flex-wrap">
            <div class="text-gray-700 m-1 w-full">Predict Diabetes</div>

            <div v-for="i in f_list" class='m-1 text-center  flex justify-center w-5/12' v-bind:key="i">
              <div>
                <label :for="i[0]" class=" m-auto text-sm font-medium text-gray-900 dark:text-white" :title="i[1]">{{
                  i[0]
                }}</label>
                <input type="text" :id="i[0]"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  :placeholder="i[0]" required>
              </div>

            </div>
            <div class='m-1 text-center  flex justify-center w-full'>
              <div>
                <label for="id" class=" m-auto text-sm font-medium text-gray-900 dark:text-white" title="id">id</label>
                <input type="text" id="id"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="id" required>
              </div>
            </div>
          </div>
          <div class="mt-3">
            <button type="submit" class="
            h-10
            px-5
            text-indigo-100
            bg-indigo-700
            rounded-lg
            transition-colors
            duration-150
            focus:shadow-outline
            hover:bg-indigo-800
          
          ">
              Upload
            </button>
          </div>

        </form>
      </div>
    </div>
    <div class=" w-auto  md:w-60 md:max-w-full mx-auto">

      <div class="p-6 border  border-gray-300 sm:rounded-md">
        <div class="flex flex-col justify-between flex-wrap">
          <div class="text-gray-700 m-2 w-full">Response</div>
          <ul v-for="index in 3" style="list-style:none;" v-bind:key="index" class="m-1">
            <li>{{r2[index-1] + ' : ' + r_list[index-1] }}</li>
            <!-- <li>{{ r_list }}</li> -->
          </ul>
        </div>
      </div>
    </div>
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
  data() {
    return {
      value: [],
      value_single: [],
      f_list: [['HighBP', '0 = no high BP 1 = high BP'], ['HighChol', '0 = no high cholesterol 1 = high cholesterol'], ['BMI', 'BMI = kg/m2'], ['Smoker', 'Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes] 0 = no 1 = yes'], ['HeartDiseaseorAttack', 'coronary heart disease (CHD) or myocardial infarction (MI) 0 = no 1 = yes'], ['PhysActivity', 'physical activity in past 30 days - not including job 0 = no 1 = yes'],
      ['Fruits', 'Consume Fruit 1 or more times per day 0 = no 1 = yes'], ['GenHlth', 'Would you say that in general your health is: scale 1-5 1 = excellent 2 = very good 3 = good 4 = fair 5 = poor'], ['PhysHlth', 'Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? scale 1-30 days'], ['DiffWalk', 'Do you have serious difficulty walking or climbing stairs? 0 = no 1 = yes'], ['Sex', '0 = female 1 = male'], ['Age', '13-level age category'], ['Education', 'Education level (EDUCA see codebook) scale 1-6 1 = Never attended school or only kindergarten 2 = Grades 1 through 8 (Elementary) 3 = Grades 9 through 11 (Some high school) 4 = Grade 12 or GED (High school graduate) 5 = College 1 year to 3 years (Some college or technical school) 6 = College 4 years or more (College graduate)'], ['Income', 'Income scale (INCOME2 see codebook) scale 1-8 1 = less than $10,000 5 = less than $35,000 8 = $75,000 or more']],
      r_list: [],
      r2: ['id', 'predict', 'predict_name']
    }
  },
  methods: {
    sendPost: function () {
      var port = window.location.host;
      var protocol = window.location.protocol;
      var url =  protocol + "//" + port + '/api/predict_all';
      console.log(url);
      const frm = new FormData();
      var f_list = this.f_list;
      console.log(f_list);
      for (var step = 0; step < f_list.length; step++) {
        var to_in = document.getElementById(f_list[step][0]).value;
        frm.append(f_list[step][0], to_in);
      }
      frm.append('id', document.getElementById('id').value);

      console.log('frm')
      axios.post(url, frm, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
        .then((Response) => {
          console.log(Response);
          var data_in = Response.data;
          var id = data_in['id'];
          var predict = data_in['predict'];
          var predict_name = data_in['predict_name'];
          
          // this.$set(this.r_list, 0, id);
          // this.$set(this.r_list, 1, predict);   
          // this.$set(this.r_list, 2, predict_name);       
          this.r_list[0] = id;
          this.r_list[1] = predict;
          this.r_list[2] = predict_name;

        })
        .catch((error) => {
          console.log(error)
        })


    }
  }

}
</script>
