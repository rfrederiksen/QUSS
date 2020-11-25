# Finally, you may have noticed that there is a test_config.py and test_custom_funcs.py file.
# Those two modules, which I'll call "test modules",
# house tests for their respective Python modules (the config.py and custom_funcs.py files).

# Yes, I'm a big believer that data scientists should be writing tests for their code.
# Now, these tests don't have to be software-engineer-esque, production-ready tests.
# The bare minimum is just a single example that shows exactly what you're trying to accomplish with the function.
# If you accidentally break the function, the test will catch it for you.
# That's all a test is, and the single example is all that the "bare minimum test" has to cover.