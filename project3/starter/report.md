Claudio Lopez  
Professor’s Wu
ET721
11.15.2026

# Report: The Benefits of Comprehensive Testing in Software Development

## Before and After: Results Summary

* What was the initial test coverage? 
    The inital code withing test_models was asserting/testing if we were able to POST things into the dict 'Fruits', aka making an object in Fruits class. Another test included the calculation of total fruits method inside the 'FruitMetrics' class, the same test also raising a AssertionError.
## Untested Code: Effects

* Were you able to understand all features and different use cases of the code without the tests?
    Yeah, when looking over the features and use cases in the code I was able understand the entirely of the app without having to look over the tests.
* What did you think of having to test the API manually? 
    It would seem redundant and inefficient as opposed to using CI or automated testing. 
* What was the result of having few tests on your understanding of the API?
    It didnt really result in having few tests, it was harder to verify how the API behaved in certain situations and to fully understand its functionality.

## Adding Tests

* How did you go about adding more tests to the code?
    I reviewed all the areas that were not tested then created additional test cases to cover normal behavior, edge cases, and error so the API behaved as expected. 
* What is the difference between a unit test and an API test? Do they bring different values?
    A unittest focuses on a code such as a function and API test figures how the API behaves as a whole by sending requests. They provide different values because unittest helps identify issues within specific parts, while API tests makees sure that the overall system functions correctly from the user's point of view.

## Automation

* What were the benefits of automating test coverage?
    Automating test coverage made it easier to repeatedly verify that the code worked correctly after changes were made. It reduced the time required for manual testing and helped catch bugs earlier and increased confidence that existing tests were not broken.

## New Features

* What was your experience like having to add new features when you tested baseline code?
    Testing the baseline code first helped me understand the existing functionality before making changes. This made it easier to add new features because I had a clearer understanding of how the system was expected to behave.
* Did it give you any feeling of security when trying out new features?
    Yeah having the tests in one place provided help that I would need to make changes verify whether I had broken existing code. This made experimenting with new features less risky.
## Future

* What do you hope to takeaway from the experience having to write tests?
    I hope to take away the use of writing tests early and test the coverage throughout coding. This experience shows me that tests improve code reliability and make debugging easier.
