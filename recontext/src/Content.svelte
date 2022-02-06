<script>
    import ContentItem from './ContentItem.svelte';
    let articles = [
        {
            title:"Vaccine confidence in the time of COVID-19",
            sentences:"We call for a re-imagination of the culture of public health and the meaning of vaccine safety regulations. Public confidence in vaccination programs depends on the work they do for the community, rather than just the delivery of vaccine technology.",
            tags:["community","vaccine"],
            cited:6
        },
        {
            title:"Political and legal aspects of the COVID-19",
            sentences:"The authors of the article analyze the impact of the global COVID-19 pandemic on the transport and logistics sector. The research is interdisciplinary in nature. The purpose of the study is to identify and briefly characterize new ...",
            tags:["transport","logistics"],
            cited:32
        },
        {
            title:"Privacy Concerns Raised by the COVID-19 Pandemic",
            sentences:"COVID-19 has hugely changed our lives, work, and interactions with people.\nWith more and more online activities, people are easily exposed to privacy\nthreats. In this paper, we explore how users self-disclose on social media and privacy concerns raised from these behaviors.",
            tags:["privacy","self"],
            cited:12
        }
    ]
</script>

<div>
    {#each articles as article}
        <ContentItem title={article.title} 
        sentences={article.sentences} 
        tags={article.tags}
        cited={article.cited} />
    {/each}
</div>
