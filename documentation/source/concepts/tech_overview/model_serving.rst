.. _model_serving:

Model Serving
=============

stellar is a set of `two` self-contained processes that are designed to run alongside your application
servers (or on a separate host connected via a network). The first process is designated to manage low-level
networking and HTTP related comcerns, and the other process is for model serving, which helps stellar make
intelligent decisions about the incoming prompts. The model server is designed to call the purpose-built
LLMs in stellar.

.. image:: /_static/img/stellar -system-stellar itecture.jpg
   :align: center
   :width: 40%


stellar' is designed to be deployed in your cloud VPC, on a on-premises host, and can work on devices that don't
have a GPU. Note, GPU devices are need for fast and cost-efficient use, so that stellar (model server, specifically)
can process prompts quickly and forward control back to the applicaton host. There are three modes in which stellar
can be configured to run its **model server** subsystem:

Local Serving (CPU - Moderate)
------------------------------
The following bash commands enable you to configure the model server subsystem in stellar to run local on device
and only use CPU devices. This will be the slowest option but can be useful in dev/test scenarios where GPUs
might not be available.

.. code-block:: console

    $ stellar up --local-cpu

Cloud Serving (GPU - Blazing Fast)
----------------------------------
The command below instructs stellar to intelligently use GPUs locally for fast intent detection, but default to
cloud serving for function calling and guardails scenarios to dramatically improve the speed and overall performance
of your applications.

.. code-block:: console

    $ stellar up

.. Note::
    stellar's model serving in the cloud is priced at $0.05M/token (156x cheaper than GPT-4o) with averlage latency
    of 200ms (10x faster than GPT-4o). Please refer to our :ref:`Get Started <quickstart>` to know
    how to generate API keys for model serving
