def overlap(field1, field2):
    left1, bottom1, top1, right1 = field1
    left2, bottom2, top2, right2 = field2
    
    overlap_left=max(left1, left2)
    overlap_bottom=max(bottom1, bottom2)
    overlap_right=min(right1, right2)
    overlap_top=min(top1, top2)
    # Here's our wrong code again
    overlap_height=(overlap_top-overlap_bottom)
    overlap_width=(overlap_right-overlap_left)
    
    return overlap_height*overlap_width
