<template>
    <div class="main">
        <span class="candidate_header nehru">nehru house captain</span>
        <div class="candidate_container" id="captains"> 
            <div class="candidate" v-for="captain in captains" :key="captain.name" :value="captain.name">
                <img src="@/assets/user.png">
                <span>{{ captain.name }}</span>
            </div>
        </div>
        <span class="candidate_header nehru">nehru house vice captain</span>
        <div class="candidate_container" id="vice_captains">
            <div class="candidate" v-for="viceCaptain in viceCaptains" :key="viceCaptain.name" :value="viceCaptain.name">
                <img src="@/assets/user.png">
                <span>{{ viceCaptain.name }}</span>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "NehruHouse",
    props: {
        captains: Object,
        viceCaptains: Object
    }
}
</script>