<template>
  <div class="main_bg" :class="house">
    <TagoreHouse :captains="captains" :viceCaptains="vice_captains" v-if="house == 'tagore'"/>
    <TeresaHouse :captains="captains" :viceCaptains="vice_captains" v-if="house == 'teresa'"/>
    <GandhiHouse :captains="captains" :viceCaptains="vice_captains" v-if="house == 'gandhi'"/>
    <NehruHouse :captains="captains" :viceCaptains="vice_captains" v-if="house == 'nehru'"/>
  </div>
</template>

<script>
import GandhiHouse from './components/GandhiHouse.vue';
import TagoreHouse from './components/TagoreHouse.vue';
import TeresaHouse from './components/TeresaHouse.vue';
import NehruHouse from './components/NehruHouse.vue';
export default {
  name: 'App',
  components: {
    TagoreHouse,
    TeresaHouse,
    GandhiHouse,
    NehruHouse
  },
  data: function () {
    return {
      house: "tagore",
      captains:[],
      vice_captains: [],
    };
  },
  mixins: [
        require('./preload.js')
  ], 
  mounted() {

    // import json data for candidate list
    // set local variables

    const data = require('./candidates.json')
    const house = this.house
    
    // now restrict data to the required house. this will be fed into the visible house component
    if (house == "tagore") {
      this.captains = data.tagore.captains;
      this.vice_captains = data.tagore.vice_captains
    } else if (house == "teresa") {
      this.captains = data.teresa.captains;
      this.vice_captains = data.teresa.vice_captains
    } else if (house == "gandhi") {
      this.captains = data.gandhi.captains;
      this.vice_captains = data.gandhi.vice_captains
    } else if (house == "nehru") {
      this.captains = data.nehru.captains;
      this.vice_captains = data.nehru.vice_captains
    }

    // loop through every element in the DOM with the class "candidate". this gives us every candidate's element
    let candidates = document.querySelectorAll(".candidate");
    for(let i = 0; i < candidates.length; i++) {
      // check if element belongs to captains or vice captains
      if (candidates[i].parentElement.id == "captains") {
        // listen for the click event on the div
        candidates[i].addEventListener('click', () => {
          // voting logic
            alert(`voted for CAPTAIN ${candidates[i].children[1].innerText}`);
        })
      } else if (candidates[i].parentElement.id == "vice_captains") {
        // listen for the click event on the div
        candidates[i].addEventListener('click', () => {
          // voting logic
            alert(`voted for VICE CAPTAIN ${candidates[i].children[1].innerText}`);
        })
      }
    }
  }
}
</script>

<style>
@import url('/src/assets/style.css');
@import url('https://fonts.googleapis.com/css2?family=Kumbh+Sans:wght@100..900&display=swap');

* {
  font-family: "Kumbh Sans", sans-serif;
  margin: 0;
}
</style>
