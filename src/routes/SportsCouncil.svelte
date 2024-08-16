<script>
    import axios from "axios";
    import { onMount } from "svelte";

    let councilInfo = {};
    let members = [];

    onMount(async () => {
        try {
            const infoResponse = await axios.get("http://localhost:8000/council_info");
            console.log("HEL");
            councilInfo = infoResponse.data;
            console.log(councilInfo);
            console.log(councilInfo.council_name);

            const membersResponse = await axios.get("http://localhost:8000/members");
            members = membersResponse.data;
        } catch (error) {
            console.error("Error fetching data:", error);
        }
    });
</script>

<style>
    .council-info, .members-list {
        margin: 20px;
    }
    .member-card {
        border: 1px solid #ccc;
        padding: 10px;
        margin-bottom: 10px;
    }
</style>

<div class="council-info">
    <h1>{councilInfo.council_name}</h1>
    <p>{councilInfo.description}</p>
</div>

<div class="members-list">
    <h2>Members</h2>
    {#each members as member}
        <div class="member-card">
            <h3>{member.name}</h3>
            <p><strong>Position:</strong> {member.position}</p>
            <p><strong>Email:</strong> {member.email}</p>
        </div>
    {/each}
</div>
