.. _overview:


Overview
============
Welcome to stellar, the intelligent prompt gateway designed to help developers build **fast**, **secure**, and **personalized** generative AI apps at ANY scale.
In this documentation, you will learn how to quickly set up stellar to trigger API calls via prompts, apply prompt guardrails without writing any application-level logic,
simplify the interaction with upstream LLMs, and improve observability all while simplifying your application development process.

.. figure:: /_static/img/stellar _network_diagram_high_level.png
   :width: 100%
   :align: center

   High-level network flow of where stellar Gateway sits in your agentic stack. Designed for both ingress and egress prompt traffic.


Get Started
-----------

This section introduces you to stellar and helps you get set up quickly:

.. grid:: 3

    .. grid-item-card:: :octicon:`apps` Overview
        :link: overview.html

        Overview of stellar and Doc navigation

    .. grid-item-card:: :octicon:`book` Intro to stellar
        :link: intro_to_stellar .html

        Explore stellar's features and developer workflow

    .. grid-item-card:: :octicon:`rocket` Quickstart
        :link: quickstart.html

        Learn how to quickly set up and integrate


Concepts
--------

Deep dive into essential ideas and mechanisms behind stellar:

.. grid:: 3

    .. grid-item-card:: :octicon:`package` Tech Overview
        :link: ../concepts/tech_overview/tech_overview.html

        Learn about the technology stack

    .. grid-item-card:: :octicon:`webhook` LLM Provider
        :link: ../concepts/llm_provider.html

        Explore stellar’s LLM integration options

    .. grid-item-card:: :octicon:`workflow` Prompt Target
        :link: ../concepts/prompt_target.html

        Understand how stellar handles prompts


Guides
------
Step-by-step tutorials for practical stellar use cases and scenarios:

.. grid:: 3

    .. grid-item-card:: :octicon:`shield-check` Prompt Guard
        :link: ../guides/prompt_guard.html

        Instructions on securing and validating prompts

    .. grid-item-card:: :octicon:`code-square` Function Calling
        :link: ../guides/function_calling.html

        A guide to effective function calling

    .. grid-item-card:: :octicon:`issue-opened` Observability
        :link: ../guides/observability/observability.html

        Learn to monitor and troubleshoot stellar


Build with stellar
---------------

For developers extending and customizing stellar for specialized needs:

.. grid:: 2

    .. grid-item-card:: :octicon:`dependabot` Agentic Workflow
        :link: ../build_with_stellar /agent.html

        Discover how to create and manage custom agents within stellar

    .. grid-item-card:: :octicon:`stack` RAG Application
        :link: ../build_with_stellar /rag.html

        Integrate RAG for knowledge-driven responses
