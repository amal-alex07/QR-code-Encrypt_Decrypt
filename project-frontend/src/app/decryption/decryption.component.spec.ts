import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DecryptionComponent } from './decryption.component';

describe('DecryptionComponent', () => {
  let component: DecryptionComponent;
  let fixture: ComponentFixture<DecryptionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DecryptionComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DecryptionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
