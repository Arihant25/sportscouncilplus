<script>
    import axios from "axios";
    import { onMount } from "svelte";
    import { fade, fly } from "svelte/transition";

    let councilInfo = {};
    let members = [];

    onMount(async () => {
        try {
            const infoResponse = await axios.get(
                "http://localhost:8000/council_info",
            );
            councilInfo = infoResponse.data;

            const membersResponse = await axios.get(
                "http://localhost:8000/members",
            );
            members = membersResponse.data[0]["members"];
        } catch (error) {
            console.error("Error fetching data:", error);
        }
    });
</script>

<div class="container">
    <div class="council-info" in:fade={{ duration: 1000 }}>
        <h1>{councilInfo.council_name}</h1>
        <p>{councilInfo.description}</p>
    </div>

    <div class="members-list">
        <h2>Members</h2>
        {#each members as member, i}
            <div
                class="member-card"
                in:fly={{ y: 50, duration: 500, delay: i * 100 }}
            >
                <div class="member-image"></div>
                <div class="member-info">
                    <h3>{member.name}</h3>
                    <p class="position">{member.position}</p>
                    <p class="email">{member.email}</p>
                </div>
            </div>
        {/each}
    </div>
</div>

<style>
    :global(body) {
        background-color: #f0f4f8;
        font-family: "Arial", sans-serif;
        color: #333;
        line-height: 1.6;
    }

    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
    }

    .council-info {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }

    .council-info h1 {
        color: #2c3e50;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }

    .council-info p {
        font-size: 1.1rem;
        color: #34495e;
    }

    .members-list h2 {
        color: #2c3e50;
        font-size: 2rem;
        margin-bottom: 1.5rem;
        text-align: center;
    }

    .member-card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        display: flex;
        align-items: center;
        transition:
            transform 0.3s ease,
            box-shadow 0.3s ease;
    }

    .member-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }

    .member-image {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        background-color: #3498db;
        margin-right: 1.5rem;
    }

    .member-info {
        flex-grow: 1;
    }

    .member-card h3 {
        color: #2c3e50;
        font-size: 1.4rem;
        margin-bottom: 0.5rem;
    }

    .position {
        color: #3498db;
        font-weight: bold;
        margin-bottom: 0.25rem;
    }

    .email {
        color: #7f8c8d;
    }

    @media (max-width: 768px) {
        .container {
            padding: 1rem;
        }

        .member-card {
            flex-direction: column;
            text-align: center;
        }

        .member-image {
            margin-right: 0;
            margin-bottom: 1rem;
        }
    }
</style>
