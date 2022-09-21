---
sidebar_position: 3
---

# Schedule
```
gantt
    dateFormat  YYYY-MM-DD
    title       Project Schedule

    %% (`excludes` accepts specific dates in YYYY-MM-DD format, days of the week ("sunday") or "weekends", but not the word "weekdays".)

    section Elaboration Phase
    Completed task            :done,    des1, 2022-09-06,2022-09-11
    Refinement of features for MS Demo 1: desA, 2022-09-20, 3d 
    Review of features for MS Demo 1: desA, 2022-10-09, 3d 

    section Construction Phase
    MongoDB add images :         des5, 2022-09-22, 5d
    Classifier for labeling images: des51, after des5, 7d
    Upload labeled data to MongoDB: des52, after des51, 2d
    Implement liking/disliking system: des 6, after des5, 5d
    Spike on StockX API Integration: des7, 2022-09-22, 3d
    Upload labeled StockX pieces to MongoDB: des71,  after des7, 2d 
    Implement Wardrobe page: des53, after des5, 5d
    Dummy recommendations page: des72, after des71, 5d
    Navigation between pages: des8, after des53, 5d
    Django Unit tests: des9, 2022-10-09, 3d
    Manual testing: des10, after des9, 2d
    Bug fixes: after des10, 4d

section Demo Dates
   Milestone Demo 1                 :milestone, 2022-10-18, 0d
   Milestone Demo 2                 :milestone, 2022-11-01, 0d
   Milestone Demo 3                 :milestone, 2022-11-15, 0d
   Final Demo                   :milestone, 2022-12-01, 0d
```
