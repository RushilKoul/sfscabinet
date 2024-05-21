<template>
  <div class="main_bg" :class="house">
    <TagoreHouse v-if="house == 'tagore'"/>
    <TeresaHouse v-if="house == 'teresa'"/>
    <GandhiHouse v-if="house == 'gandhi'"/>
    <NehruHouse v-if="house == 'nehru'"/>
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
      house: "nehru",
      captains:[],
      vice_captains: [],
    };
  },
  mixins: [
        require('./preload.js')
  ], 
  mounted() {

    // import json data for candidate list
    const data = require('./candidates.json')
    const house = this.house
    // set local variables

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

    // define variables (again) for simpler access
    let captains = this.captains
    let vice_captains = this.vice_captains
    
    // define parent elements
    let caps = document.querySelector("#captains")
    let vcaps = document.querySelector("#vice_captains")
    
    // populate the page with candidate elements

    //captains
    for (let i = 0; i < captains.length; i++) {
      let l = document.createElement("div")
      l.classList.add("candidate")
      l.innerHTML = `
      <img src="data:image/png;base64,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">
      <span>${captains[i].name}</span>
      `
      caps.appendChild(l)
    }

    //vice captains
    for (let i = 0; i < vice_captains.length; i++) {
      let l = document.createElement("div")
      l.classList.add("candidate")
      l.innerHTML = `
      <img src="data:image/png;base64,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">
      <span>${vice_captains[i].name}</span>
      `
      vcaps.appendChild(l)
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
