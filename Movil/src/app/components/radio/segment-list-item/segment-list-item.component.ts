import { ChangeDetectorRef, Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { SegmentItem } from 'app/shared/Segment';

@Component({
  selector: 'app-segment-list-item',
  templateUrl: './segment-list-item.component.html',
  styleUrls: ['./segment-list-item.component.scss'],
})
export class SegmentListItemComponent implements OnInit {
  @Input() idSegment: number;
  @Input() nameSegment: string;
  @Input() image: string;
  @Input() startHour: string;
  @Input() finishHour: string;

  @Input() currentSegment: SegmentItem;

  active = false;

  constructor(private router: Router, private changeDetector: ChangeDetectorRef) {
    this.active = false;
  }

  ngOnInit() {}

  toggleNotification() {
    if(this.active){
      this.active = false;
    }
    else{
      this.active = true;
    }
    this.changeDetector.detectChanges();
    console.log(this.idSegment);
  }

  openProgramInfo() {
    this.router.navigate(['/programming',this.idSegment]);
  }

}
